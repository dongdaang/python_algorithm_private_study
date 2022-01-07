import sys
input = sys.stdin.readline

N = int(input())
card = list(map(int, input().split()))
M = int(input())
num = list(map(int, input().split()))

card_list = [0] * 20000001
num_list = [0] * 20000001
result = []

for i in card:
    card_list[i+10000000] += 1

for i in num:
    result.append(card_list[i+10000000])

print(*result)



# 정답예시 코드(이진탐색)
# from sys import stdin
# _ = stdin.readline()
# N = sorted(map(int,stdin.readline().split()))
# _ = stdin.readline()
# M = map(int,stdin.readline().split())

# def binary(n, N, start, end):
#     if start > end:
#         return 0
#     m = (start+end)//2
#     if n == N[m]:
#         return N[start:end+1].count(n)
#     elif n < N[m]:
#         return binary(n, N, start, m-1)
#     else:
#         return binary(n, N, m+1, end)

# n_dic = {}
# for n in N:
#     start = 0
#     end = len(N) - 1
#     if n not in n_dic:
#         n_dic[n] = binary(n, N, start, end)

# print(' '.join(str(n_dic[x]) if x in n_dic else '0' for x in M ))