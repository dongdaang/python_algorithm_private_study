import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
if M == 0:
    print(min(abs(N - 100), len(str(N))))
else:
    broken_button = list(map(int, input().split()))
    res = abs(100 - N)
    for i in range(1000001):
        i = str(i)
        for j in range(len(i)):
            if int(i[j]) in broken_button:
                break
            elif j == len(i) - 1:
                res = min(res, abs(int(i) - N) + len(i))
    print(res)