import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
res = []
for _ in range(T):
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    build_order = [[] for _ in range(N + 1)]
    cnt = [0] * (N + 1)
    dp = [0] * (N + 1)
    for _ in range(K):
        X, Y = map(int, input().split())
        build_order[X].append(Y)
        cnt[Y] += 1
    W = int(input())
    
    queue = deque()
    for i in range(1, N + 1):
        if cnt[i] == 0:
            queue.append(i)
            dp[i] = D[i - 1]
    
    while queue:
        current = queue.popleft()
        for i in build_order[current]:
            cnt[i] -= 1
            dp[i] = max(dp[current] + D[i - 1], dp[i])
            if cnt[i] == 0:
                queue.append(i)
    res.append(dp[W])
    
for i in res:
    print(i)