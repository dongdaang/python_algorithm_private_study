N = int(input())
p = list(map(int, input().split()))

p.sort()
tmp = 0
total = []
for i in p:
    tmp += i
    total.append(tmp)

print(sum(total))



# 정답코드 예시
# N = int(input())
# delay = list(map(int, input().split()))
# delay.sort()
# sum = 0
# for i in range(N):
#     sum += delay[i]*(N-i)

# print(sum)