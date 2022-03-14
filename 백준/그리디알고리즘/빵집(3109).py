import sys
input = sys.stdin.readline

R, C = map(int, input().split())
graph = [[i for i in input().rstrip()] for _ in range(R)]

dx = [-1, 0, 1]
res = 0
def dfs(x, y):
    global res, flag
    y += 1
    if y == C - 1:
        res += 1
        flag = True
        return
    for i in range(3):
        nx = x + dx[i]
        if nx < 0 or nx >= R or graph[nx][y] != '.':
            continue
        dfs(nx, y)
        if flag == True:
            graph[nx][y] = 'o'
            return
        else:
            graph[nx][y] = 'o'
    y -= 1

for i in range(R):
    flag = False
    dfs(i, 0)

print(res)