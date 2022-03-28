import sys
input = sys.stdin.readline

G = int(input())
P = int(input())
planes = [int(input()) for _ in range(P)]
gates = [False] * G
a = [0] * (G + 1)
res = 0
for i in planes:
    a[i] += 1
tmp = []
for i in set(planes):
    j = i - 1
    for _ in range(a[i]):
        if j >= 0:
            tmp.append(j)
            j -= 1
for i in tmp:
    if gates[i] == False:
        gates[i] = True
        res += 1
    else:
        break
print(res)