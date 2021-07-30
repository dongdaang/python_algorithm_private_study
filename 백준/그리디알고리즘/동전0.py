N, K = map(int, input().split())

coins = []
money_sum = 0
total = 0

for _ in range(N):
    coin = int(input())
    coins.append(coin)

for i in range(len(coins)-1, -1, -1):
    if coins[i] <= K - money_sum:
        cnt = 0
        while True:
            cnt += 1
            money = coins[i] * cnt
            if money >= K - money_sum:
                break
        if money > K - money_sum:
            money -= coins[i]
            money_sum += money
            cnt -= 1
            total += cnt
        elif money == K - money_sum:
            money_sum += money
            total += cnt
    if money_sum == K:
        break
print(total)

# N, K = map(int, input().split())
# A = []
# for i in range(N):
#     A.append(int(input()))

# count = 0
# for i in range(N-1, -1, -1):
#     if K == 0:
#         break
#     count += K // A[i]
#     K %= A[i]

# print(count)