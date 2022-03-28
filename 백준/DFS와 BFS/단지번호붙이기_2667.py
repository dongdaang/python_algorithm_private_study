import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N)]
for i in range(N):
    a = input()
    for j in range(N):
        graph[i].append(int(a[j]))

cnt = 0

def dfs(x, y):
    global cnt
    if graph[x][y] != 0:
        graph[x][y] = 0
        cnt += 1
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= 0 and nx < N and ny >= 0 and ny < N:
                dfs(nx, ny)

result = []

for i in range(N):
    for j in range(N):
        dfs(i, j)
        if cnt != 0:
            result.append(cnt)
            cnt = 0
result.sort()
print(len(result))
for i in result:
    print(i)