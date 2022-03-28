import sys
from collections import deque
input = sys.stdin.readline

def bfs(a, b):
    queue = deque([(a, b)])
    visited[a][b] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M or visited[nx][ny] == True:
                continue
            if graph[nx][ny] == 'L':
                tmp[nx][ny] = tmp[x][y] + 1
                visited[nx][ny] = True
                queue.append((nx, ny))

N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = []

for i in range(N):
    for j in range(M):
        if graph[i][j] == 'L':
            tmp = [[0] * M for _ in range(N)]
            visited = [[False] * M for _ in range(N)]
            bfs(i, j)
            res = max(max(tmp[a]) for a in range(N))
            ans.append(res)
print(max(ans))