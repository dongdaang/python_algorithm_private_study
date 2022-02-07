import sys
input = sys.stdin.readline

N = int(input())
l = []
for _ in range(N):
    l.append(int(input()))
l.sort(reverse=True)
result = 0
for i in range(len(l)):
    if l[i] * (i + 1) > result:
        result = l[i] * (i + 1)
print(result)