import sys, heapq
input = sys.stdin.readline

N = int(input())
card = []
for _ in range(N):
    heapq.heappush(card, int(input()))

sum = 0

while len(card) > 1:
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    sum += a + b
    heapq.heappush(card, a + b)
print(sum)