import sys

times = []
tmp = []

N = int(input())
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    times.append([a,b])

def f(s):
    for i in times:
        if i[0] == s[0]:
            if i[1] < s[1]:
                s = i
    tmp.append(s)