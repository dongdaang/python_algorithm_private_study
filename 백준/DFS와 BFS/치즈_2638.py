import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
res = 0

while True:
    queue = deque()
    check = [[0] * M for _ in range(N)]
    check[0][0] = 1
    queue.append((0, 0))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not check[nx][ny]:
                if grid[nx][ny]:
                    grid[nx][ny] += 1
                else:
                    check[nx][ny] = 1
                    queue.append((nx, ny))
        
    flag = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] >= 3:
                grid[i][j] = 0
            elif grid[i][j] > 0:
                grid[i][j] = 1
                flag = 1
    
    res += 1
    
    if not flag:
        print(res)
        break