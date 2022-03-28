import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
queue = deque([N])
dist = [0] * 100001

def bfs():
    while queue:
        pos = queue.popleft()
        
        if pos == K:
            return dist[pos]
        
        for i in (pos - 1, pos + 1, pos * 2):
            if 0 <= i <= 100000 and not dist[i]:
                dist[i] = dist[pos] + 1
                queue.append(i)

print(bfs())