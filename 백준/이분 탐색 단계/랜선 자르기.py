import sys

l = []

K, N = map(int, input().split())
for _ in range(K):
    a = int(sys.stdin.readline().rstrip())
    l.append(a)
start, end = 1, max(l)

while start <= end:
    mid = int((start + end) / 2)
    lines = 0
    for i in l:
        lines += int(i / mid)
    if lines >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)