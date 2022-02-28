# import sys
# input = sys.stdin.readline

# N = int(input())
# weights = list(map(int, input().split()))
# weights.sort()
# res = []
# l, r = 0, 0
# for weight in weights:
#     if weight not in res:
#         res.append(weight)
# while l < len(weights) and r < len(weights):
#     if l == len(weights):
#         r += 1
#     elif r == len(weights):
#         l += 1
#     else:
#         if weights[l] + weights[r] not in res:
#             res.append(weights[l] + weights[r])
#         if sum(weights[l:r + 1]) not in res:
#             res.append(sum(weights[l:r + 1]))
#         if weights[l] + weights[r] < sum(weights[l:r + 1]):
#             l += 1
#         else:
#             r += 1
# ans = 0
# for i in range(1, len(res)):
#     if res[i] == 0:
#         ans = i
#         break
# res.sort()
# print(res)

N = int(input())
arr = [int(i) for i in input().split()]
arr.sort()
total = 0
for i in range(N):
    if total + 1 >= arr[i] :
        total += arr[i]
    else:
        break

print(total + 1)