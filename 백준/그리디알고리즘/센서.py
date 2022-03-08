import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
coordinates = list(map(int, input().split()))
if K >= N:
    print(0)
else:
    coordinates.sort()
    d = []
    for i in range(1, N):
        d.append(coordinates[i] - coordinates[i - 1])
    d.sort()
    for _ in range(K - 1):
        d.pop()
    print(sum(d))