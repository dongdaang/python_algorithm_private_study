import sys

N = int(input())
a = [0] * 8001      #index 0 : -4000  index 4000 : 0  index 8000 : 4000
b = []
c = []
sum = 0
cnt = 0
for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    a[num + 4000] += 1
for i in range(len(a)):
    if i != 0:
        sum += (i - 4000) * a[i]
        cnt += a[i]
print(round(sum / N))

for i in range(len(a)):
    if i != 0:
        if cnt - a[i] <= round(cnt / 2):
            print(i - 4000)
            break
        else:
            cnt -= a[i]

for i in range(len(a)):
    if a[i] == max(a):
        b.append(i)
if len(b) == 1:
    print(b[0] - 4000)
else:
    print(b[1] - 4000)

for i in range(len(a)):
    if a[i] != 0:
        num_1 = i - 4000
        break
for i in range(len(a)):
    if a[i] != 0:
        num_2 = i - 4000
print(num_2 - num_1)