import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(a):
    heap = []
    d = [INF] * (N + 1)
    d[a] = 0
    heapq.heappush(heap, (0, a))
    
    while heap:
        distance, current = heapq.heappop(heap)
        if d[current] < distance:
            continue
        for next, weight in graph[current]:
            next_distance = distance + weight
            if next_distance < d[next]:
                d[next] = next_distance
                heapq.heappush(heap, (next_distance, next))
    return d
    
N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))                 #시작점이 한 곳이 아니라 여러곳이므로
    graph[b].append((a, c))                 #기본 다익스트라와 달리 a->b 와 b->a의 경우를 모두 넣어줘야 함
v1, v2 = map(int, input().split())

start = dijkstra(1)
point1 = dijkstra(v1)
point2 = dijkstra(v2)

res = min(start[v1] + point1[v2] + point2[N], start[v2] + point2[v1] + point1[N])
print(res if res < INF else -1)