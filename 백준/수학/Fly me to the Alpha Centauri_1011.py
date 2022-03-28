import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x, y = map(int,input().split())
    distance = y - x
    cnt = 0
    power = 1
    while distance > 0:
        cnt += 1
        distance -= power
        if cnt % 2 == 0:
            power += 1  
    print(cnt)