import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx >= 0 and nx < N and ny >= 0 and ny < M and graph[nx][ny] == 0:
            graph[nx][ny] = 1
            queue.append([nx, ny])

queue = deque([])

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append([i, j])

cnt = 0

while queue:
    for _ in range(len(queue)):
        bfs()
    cnt += 1

def ans():
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                return -1
    return cnt-1

print(ans())