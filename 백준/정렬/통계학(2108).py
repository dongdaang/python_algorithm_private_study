import sys
input = sys.stdin.readline

N = int(input())
num = [0] * 8001
sum = 0
mid = 0
max = 0
cnt1 = 0
cnt2 = 0
tmp = 0
start = 0
finish = 0
for _ in range(N):
    a = int(input())
    num[a + 4000] += 1

for i in range(len(num)):
    if num[i] != 0:
        cnt1 += num[i]
        sum += (i - 4000) * num[i]
avg = round(sum / cnt1)

for i in range(len(num)):
    if num[i] != 0:
        cnt2 += num[i]
        if cnt2 >= int(N / 2) + 1:
            mid = i - 4000
            break

for i in range(len(num)):
    if num[i] != 0:
        if num[i] > max:
            max = num[i]
for i in range(len(num)):
    if num[i] == max:
        tmp += 1
        if tmp == 2:
            result = i - 4000
            break
        result = i - 4000

for i in range(0, len(num)):
    if num[i] != 0:
        start = i - 4000
        break
for i in range(len(num)-1, -1, -1):
    if num[i] != 0:
        finish = i - 4000
        break

print(avg)
print(mid)
print(result)
print(finish-start)