import sys
input = sys.stdin.readline

S1 = input().rstrip()
S2 = input().rstrip()
matrix = [[0] * (len(S2) + 1) for _ in range(len(S1) + 1)]

for i in range(1, len(S1) + 1):
    for j in range(1, len(S2) + 1):
        if S1[i - 1] == S2[j - 1]:
            matrix[i][j] = matrix[i - 1][j - 1] + 1
        else:
            matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

print(matrix[-1][-1])



#############좀 더 간단한 풀이(1차원 dp)##############

s1 = input()
s2 = input()

len_s1, len_s2 = len(s1), len(s2)
dp = [0] * (len_s1)

for i in range(len_s2):
    cnt = 0
    for j in range(len_s1):
        if cnt < dp[j]:
            cnt = dp[j]
        elif s2[i] == s1[j]:
            dp[j] = cnt + 1
print(dp)