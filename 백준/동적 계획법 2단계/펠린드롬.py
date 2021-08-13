# import sys                        시간초과된 코드....

# def p(a, i, j, s):
#     if i < (s - 1):
#         return 1
#     elif a[i] == a[j]:
#         return p(a, i-1, j-1, s)
#     else:
#         return 0

# N = int(input())
# a = list(map(int, input().split()))
# M = int(input())

# for _ in range(M):
#     S, E = map(int, sys.stdin.readline().rstrip().split())
#     t = ((E + S) // 2) - 1
#     if (E + S) % 2 == 0:
#         result = p(a, t-1, t+1, S)
#         print(result)
#     elif (E + S) % 2 == 1:
#         result = p(a, t, t+1, S)
#         print(result)

import sys

n = int(input())

d = [int(i) for i in sys.stdin.readline().split()]
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    dp[i][i] = 1

for i in range(n-1):
    if d[i] == d[i+1]:
        dp[i][i+1] = 1

for l in range(2, n):
    for i in range(n-l):
        if d[i] == d[i+1] and dp[i+1][i+l-1] == 1:
            dp[i][i+l] = 1

m = int(input())

for _ in range(m):
    i, j = [int(a) for a in sys.stdin.readline().split()]
    print(dp[i-1][j-1])