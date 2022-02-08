import sys
input = sys.stdin.readline

M, N, K = map(int, input().split())
graph = [[0 for _ in range(N)] for _ in range(M)]
for _ in range(K):
    coordinate = list(map(int, input().split()))
    x1, y1 = coordinate[0], coordinate[1]
    x2, y2 = coordinate[2], coordinate[3]
    for i in range(M-y2, M-y1):
        for j in range(x1, x2):
            if graph[i][j] == 0:
                graph[i][j] = 1

def dfs(x, y):
    space = 0
    if x <= -1 or x >= 5 or y <= -1 or y >= N:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        space += 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        result = [True, space]
        return result
    return False

ans = 0
total_space = 0

for i in range(M):
    for j in range(N):
        if dfs(i, j)[0] == True:
            ans += 1
            total_space += dfs(i, j)[1]
print(ans)
print(total_space)