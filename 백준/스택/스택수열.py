n = int(input())
s = []
a = []
cnt = 1
tmp = True

for _ in range(n):
    num = int(input())
    while cnt <= num:
        s.append(cnt)
        a.append('+')
        cnt += 1
    if s[-1] == num:
        s.pop()
        a.append('-')
    else:
        tmp = False
if tmp == False:
    print('NO')
else:
    for i in a:
        print(i)