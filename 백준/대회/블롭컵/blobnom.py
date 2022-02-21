import sys
input = sys.stdin.readline

N = int(input())
top = list(map(int, input().split()))
tmp = []

if len(top) >= 3:
    for i in range(1, len(top)-1):
        tmp.append(min(top[i] + top[i - 1], top[i] + top[i + 1]))
    print(max(tmp))

else:
    print(max(top))