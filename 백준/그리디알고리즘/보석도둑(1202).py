import sys, heapq
input = sys.stdin.readline

N, K = map(int, input().split())
jewelry = [tuple(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]
jewelry.sort()
bags.sort()

total = 0
tmp = []

for bag in bags:
    while jewelry and bag >= jewelry[0][0]:
        heapq.heappush(tmp, -heapq.heappop(jewelry)[1])
    
    if tmp:
        total -= heapq.heappop(tmp)
    elif not jewelry:
        break
print(total)