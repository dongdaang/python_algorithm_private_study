import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
year = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    queue = deque([(i, j)])
    visited[i][j] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if visited[nx][ny] == True:
                continue
            if graph[nx][ny] <= 0:
                graph[x][y] -= 1
            else:
                queue.append((nx, ny))
                visited[nx][ny] = True

while True:
    visited = [[False] * M for _ in range(N)]
    iceberg = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0 and visited[i][j] == False:
                bfs(i, j)
                iceberg += 1
    if iceberg == 0:
        print(0)
        break
    if iceberg >= 2:
        print(year)
        break
    year += 1