#############다익스트라 알고리즘#############

import sys, heapq
input = sys.stdin.readline

INF = float('inf')
V, E = map(int, input().split())
K = int(input())
line = [[] for _ in range(V + 1)]
d = [INF] * (V + 1)
heap = []

for _ in range(E):
    u, v, w = map(int, input().split())
    line[u].append((v, w))
    
def dijkstra(a):
    d[a] = 0
    heapq.heappush(heap, (0, a))
    
    while heap:
        distance, current = heapq.heappop(heap)
        if d[current] < distance:
            continue
        for next, weight in line[current]:
            nextDistance = distance + weight
            if nextDistance < d[next]:
                d[next] = nextDistance
                heapq.heappush(heap, (nextDistance, next))
        
dijkstra(K)

for i in d[1:]:
    print('INF' if i == INF else i)