import sys, heapq
input = sys.stdin.readline

def dijkstra(a):
    d[a] = 0
    heapq.heappush(heap, (0, a))
    while heap:
        distance, current = heapq.heappop(heap)
        if d[current] < distance:
            continue
        for next, weight in line[current]:
            nextdistance = distance + weight
            if nextdistance < d[next]:
                d[next] = nextdistance
                heapq.heappush(heap, (nextdistance, next))

V, E = map(int, input().split())
K = int(input())
line = [[] for _ in range(V + 1)]
INF = float('inf')
d = [INF] * (V + 1)
heap = []

for _ in range(E):
    u, v, w = map(int, input().split())
    line[u].append((v, w))
    
dijkstra(K)

for i in d[1:]:
    print('INF' if i == INF else i)