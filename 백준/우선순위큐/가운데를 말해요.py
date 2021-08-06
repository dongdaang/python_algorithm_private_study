import sys

a = []

N = int(input())
for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    a.append(num)

for i in range(1, N+1):
    b = a[:i]
    b.sort()
    print(b[int(i-1/2)])