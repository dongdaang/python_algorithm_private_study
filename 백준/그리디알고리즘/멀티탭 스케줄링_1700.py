import sys
input = sys.stdin.readline

N, K = map(int, input().split())
multap = [0] * N
li = list(map(int, input().split()))
res = swap = num = max_I = 0
for i in li:
    if i in multap:
        pass
    elif 0 in multap:
        multap[multap.index(0)] = i
    else:
        for j in multap:
            if j not in li[num:]:
                swap = j
                break
            elif li[num:].index(j) > max_I:
                max_I = li[num:].index(j)
                swap = j
        multap[multap.index(swap)] = i
        max_I = swap = 0
        res += 1
    num += 1
print(res)