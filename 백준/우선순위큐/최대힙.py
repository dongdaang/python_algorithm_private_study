import sys

a = []
result = []
cnt = 1

N = int(input())

while cnt <= N:
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        if len(a) == 0:
            result.append(0)
        else:
            i = max(a)
            result.append(i)
            del(i)
    else:
        a.append(num)
    cnt += 1
for i in result:
    print(i)