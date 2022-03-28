import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y):
    if dp[x][y]:
        return dp[x][y]
    
    dp[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if grpah[x][y] < grpah[nx][ny]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
            
    return dp[x][y]

n = int(input())
grpah = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
result = 0
for i in range(n):
    for j in range(n):
        dfs(i ,j)
        result = max(result, dfs(i, j))
print(result)