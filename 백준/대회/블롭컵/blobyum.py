import sys
input = sys.stdin.readline

N, K = map(int, input().split())
taste = list(map(int, input().split()))

tmp = []
for i in range(K):
    tmp.append(sum(taste) - sum(taste[i:i+N-K]))
for i in range(len(taste) - K + 1):
    tmp.append(sum(taste[i:i+K]))

print(max(tmp))