import sys, heapq
input = sys.stdin.readline

n = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(n)]
schedule.sort(key=lambda x : x[1])
heap = []
total = 0
for info in schedule:
    heapq.heappush(heap, info[0])
    if len(heap) > info[1]:
        heapq.heappop(heap)
print(sum(heap))