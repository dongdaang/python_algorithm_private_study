import sys
input = sys.stdin.readline

N = int(input())
p = []
for _ in range(N):
    a = list(map(int, input().split()))
    p.append(a)
p.sort()
for i in p:
    print(i[0], i[1])

# 정답코드 예시
# import sys
# input = sys.stdin.readline
# print = sys.stdout.write

# N = int(input())
# temp = {}
# for n in range(N):
#     x, y = map(int, input().split())
#     if x in temp:
#         temp[x].append(y)
#     else:
#         temp[x] = [y]

# temp2 = sorted(temp)
# for key in temp2:
#     temp[key].sort()
#     for value in temp[key]:
#         print(str(key) + " " + str(value) + "\n")