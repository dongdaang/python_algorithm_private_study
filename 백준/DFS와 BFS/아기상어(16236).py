import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
shark_pos = None
shark_size = 2
eat_cnt = 0
fish_pos = []
fish_size = []
res = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            shark_pos = (i, j)
        elif graph[i][j] in (1, 2, 3, 4, 5 ,6):
            fish_pos.append((i, j))
for i in fish_pos:
    fish_size.append(graph[i[0]][i[1]])

def bfs():
    global eat_cnt
    shark_route = deque([shark_pos])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    flag = False
    while shark_route:
        x, y = shark_route.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N or graph[nx][ny] < 0 or graph[nx][ny] > shark_size:
                continue
            if graph[nx][ny] < shark_size:
                eat_cnt += 1
                fish_pos.remove((nx, ny))
                fish_size.remove(graph[nx][ny])
                graph[nx][ny] = graph[x][y] - 1
                flag = True
                break
            elif graph[nx][ny] == shark_size:
                shark_route.append(graph[nx][ny])
            else:
                graph[nx][ny] = graph[x][y] - 1
                shark_route.append(graph[nx][ny])
        if flag == True:
            break

while fish_pos:
    bfs()
    tmp = 0
    if eat_cnt == shark_size:
        eat_cnt = 0
        shark_size += 1
    for size in fish_size:
        if size > shark_size:
            tmp += 1
    if tmp == len(shark_size):
        break

for i in range(N):
    for j in range(N):
        if graph[i][j] < res:
            res = graph[i][j]

print(-res)