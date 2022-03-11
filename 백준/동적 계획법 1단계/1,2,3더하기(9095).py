import sys
input = sys.stdin.readline

T = int(input())
dp = [1, 2, 4]
res = []
for i in range(3, 10):
    dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])
for _ in range(T):
    n = int(input())
    res.append(dp[n - 1])
for i in res:
    print(i)