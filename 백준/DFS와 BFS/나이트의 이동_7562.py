import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def bfs(a, b, target_x, target_y):
    q = deque([[a, b]])

    while q:
        x, y = q.popleft()
        
        if x == target_x and y == target_y:
            return cnt[x][y]
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < I and 0 <= ny < I and cnt[nx][ny] == 0:
                q.append([nx, ny])
                cnt[nx][ny] = cnt[x][y] + 1
        
T = int(input())
for _ in range(T):
    I = int(input())
    a, b = map(int, input().split())
    target_x, target_y = map(int, input().split())
    cnt = [[0] * I for _ in range(I)]
    print(bfs(a, b, target_x, target_y))