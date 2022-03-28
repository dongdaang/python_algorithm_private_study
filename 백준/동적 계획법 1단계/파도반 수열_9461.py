import sys
input = sys.stdin.readline

d = [0] * 101
d[0] = 1
d[1] = 1
d[2] = 1
d[3] = 2
d[4] = 2
d[5] = 3
d[6] = 4
d[7] = 5
d[8] = 7
d[9] = 9

for i in range(10, 101):
    d[i] = d[i-1] + d[i-5]

T = int(input())
for _ in range(T):
    N = int(input())
    print(d[N-1])