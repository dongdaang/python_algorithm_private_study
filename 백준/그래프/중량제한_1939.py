import sys
from collections import deque
input = sys.stdin.readline

def bfs(mid):
    visited[factory1] = 1
    queue = deque()
    queue.append(factory1)
    
    while queue:
        now = queue.popleft()
        if now == factory2:
            return True
        
        for next, weight in graph[now]:
            if visited[next] == 0 and mid <= weight:
                queue.append(next)
                visited[next] = 1
                
    return False

N, M = map(int, input().split())
graph = [[] for i in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))
factory1, factory2 = map(int, input().split())

low, high = 1, 1000000000
while low <= high:
    visited = [0 for i in range(N + 1)]
    mid = (low + high) // 2
    if bfs(mid):
        low = mid + 1
    else:
        high = mid - 1
        
print(high)