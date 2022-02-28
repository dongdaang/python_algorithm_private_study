import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(input().rstrip()))
dp = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]

def dfs(x, y):
    distance = int(graph[x][y])
    dx = [-distance, distance, 0, 0]
    dy = [0, 0, -distance, distance]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] != 'H':
            if visited[nx][ny] == 1:
                return False
            dp[nx][ny] = dp[x][y] + 1
            visited[nx][ny] = 1
            dfs(nx, ny)
    return True

if not dfs(0, 0):
    print(-1)
else:
    max = 0
    for i in range(N):
        for j in range(M):
            if dp[i][j] > max:
                max = dp[i][j]
    print(max + 1)