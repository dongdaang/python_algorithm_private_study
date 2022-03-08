n, m = map(int, input().split())
answer = 1
for i in range(m):
    answer *= (n-i)
    answer //= (i+1)
print(int(answer))


###########DP활용 코드(파스칼 삼각형)###########
import sys
n , m = map(int, sys.stdin.readline().split(" "))
dp = [[0 for i in range(101)] for j in range(101)]
for i in range(1,101):
    dp[i][0] = 1
    dp[i][i] = 1
for i in range(2,101):
    for t in range(1,i):
        dp[i][t] = dp[i-1][t-1] + dp[i-1][t]
print(dp[n][m])