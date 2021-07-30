N = input()
cnt = 0
if int(N) >= 0 and int(N) <= 99:
    num = N
    if int(num) < 10:
         num = '0' + num
    while True:
        num = num[1] + str((int(num[0]) + int(num[1])))[-1]
        cnt += 1
        if int(num) == int(N):
            break

print(cnt)