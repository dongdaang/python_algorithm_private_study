import sys
input = sys.stdin.readline

T = int(input())
res = []
for _ in range(T):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    
    dp = [[0] * n for _ in range(2)]
    dp[0][0], dp[1][0] = sticker[0][0], sticker[1][0]
    
    for i in range(1, n):
        dp[0][i] = max(dp[0][i - 1], dp[1][i - 1] + sticker[0][i])
        dp[1][i] = max(dp[1][i-  1], dp[0][i - 1] + sticker[1][i])
    
    res.append(max(dp[0][n - 1], dp[1][n - 1]))

for i in res:
    print(i)