n, m = map(int, input("작업 수 / 작업 번호 : ").split())
p = list(map(int, input("작업 우선순위 : ").split()))

min = 0

while True:
    if p[0] == max(p):
        del(p[0])
        min += 1
        if m == 0:
            break
        else:
            m -= 1
    else:
        tmp = p[0]
        del(p[0])
        p.append(tmp)
        if m == 0:
            m += (len(p) - 1)
        else:
            m -= 1

print("{0}분".format(min))