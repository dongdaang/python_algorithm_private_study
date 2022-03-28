import sys
input = sys.stdin.readline

n = int(input())
amount = [0]
for _ in range(n):
    amount.append(int(input()))

if n == 1:
    print(amount[1])

else:
    dp = [0] * 10001
    dp[1] = amount[1]
    dp[2] = amount[2] + amount[1]

    for i in range(3, n + 1):
        dp[i] = max(dp[i - 3] + amount[i - 1] + amount[i], dp[i - 2] + amount[i], dp[i - 1])

    print(dp[n])