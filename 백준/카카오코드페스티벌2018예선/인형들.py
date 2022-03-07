import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dolls = list(map(int, input().split()))

def f(a):
    m = sum(a) / K
    tmp = 0
    for i in a:
        tmp += (i - m) ** 2
    o = (tmp / K) ** 0.5
    return o

ans = float('inf')

while K <= N:
    for i in range(N - K + 1):
        res = f(dolls[i:i+K])
        if ans > res:
            ans = res
    K += 1

print(ans)