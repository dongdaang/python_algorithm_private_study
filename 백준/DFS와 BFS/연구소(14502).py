import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
tmp1 = []
tmp2 = []
queue2 = deque()

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            continue
        if graph[i][j] == 0:
            tmp1.append((i, j))
        elif graph[i][j] == 2:
            tmp2.append((i, j))

queue1 = deque(combinations(tmp1, 3))
def bfs():
    res = 0
    while queue1:
        visited = [graph[i][:] for i in range(N)]
        cnt = 0
        a, b, c = queue1.popleft()
        visited[a[0]][a[1]] = 1
        visited[b[0]][b[1]] = 1
        visited[c[0]][c[1]] = 1
        
        queue2 = deque(tmp2)
        while queue2:
            x, y = queue2.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= M or visited[nx][ny] != 0:
                    continue
                visited[nx][ny] = 2
                queue2.append((nx, ny))
        
        for i in range(N):
            for j in range(M):
                if visited[i][j] == 0:
                    cnt += 1
        if cnt > res:
            res = cnt
    return res

print(bfs())