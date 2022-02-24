from collections import deque
import sys

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(a, b, iscrash, visited, graph):
    #crash 0: 벽안부시고 가는경우, 1: 부신 경우
    queue = deque()
    queue.append((a, b, iscrash))
    visited[a][b][iscrash] = 1

    while queue:
        x, y, iscrash = queue.popleft()
        if x == N - 1 and y == M - 1:
            return visited[x][y][iscrash]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= N or ny <= -1 or ny >= M:
                continue
            # 벽 안부수고 이동
            if graph[nx][ny] == 0 and visited[nx][ny][iscrash] == 0:
                queue.append((nx, ny, iscrash))
                visited[nx][ny][iscrash] = visited[x][y][iscrash] + 1
            # 벽 부수고 이동
            if graph[nx][ny] == 1 and iscrash == 0:
                queue.append((nx, ny, iscrash + 1))
                visited[nx][ny][iscrash + 1] = visited[x][y][iscrash] + 1

    return -1

print(bfs(0, 0, 0, visited, graph))