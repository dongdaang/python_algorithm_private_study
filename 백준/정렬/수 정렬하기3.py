import sys

N = int(input())
a = [0] * 10001
for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    a[num] += 1
for i in range(10001):
    if a[i] != 0:
        for j in range(a[i]):
            sys.stdout.write(str(i) + '\n')