import sys

N = int(input())
a = list(map(int, sys.stdin.readline().split()))
dp = [0]

for i in range(N):
    low = 0
    high = len(dp) - 1 

    while low <= high:
        mid = int((low + high) / 2)
        if dp[mid] < a[i]:
            low = mid + 1
        else:
            high = mid - 1
    if low >= len(dp):
        dp.append(a[i])
    else:
        dp[low] = a[i]
print(len(dp) - 1)