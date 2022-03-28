import sys
input = sys.stdin.readline

N, K = map(int, input().split())
t = [[0, 0]]
knapsack = [[0 for _ in range(K+1)] for _ in range(N+1)]

for _ in range(N):
    t.append(list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, K+1):
        weight = t[i][0]
        value = t[i][1]

        if j < weight:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(value + knapsack[i-1][j-weight], knapsack[i-1][j])

print(knapsack[N][K])




# 정답코드 예시
# import sys
# input = sys.stdin.readline

# n,k = map(int, input().split())
# ary = [list(map(int, input().split())) for _ in range(n)]

# dp = [0]*(k+1)
# ary.sort()
# for weight, val in ary:
#     for j in range(k, weight-1,-1):
#         dp[j] = max(dp[j], dp[j-weight] + val)

# print(dp[k])