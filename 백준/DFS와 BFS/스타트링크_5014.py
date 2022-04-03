import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    while queue:
        now, cnt = queue.popleft()
        if now == G:
            return cnt
        next_up = now + U
        next_down = now - D
        if next_up <= F and not visited[next_up]:
            queue.append((next_up, cnt + 1))
            visited[next_up] = True
        if next_down > 0 and not visited[next_down]:
            queue.append((next_down, cnt + 1))
            visited[next_down] = True
    return 'use the stairs'
        

F, S, G, U, D = map(int, input().split())

queue = deque([(S, 0)])
visited = [False] * (F + 1)
visited[S] = True

print(bfs())