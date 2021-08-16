import sys

input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
x = int(input())
cnt = 0

num.sort()

left = 0
right = n - 1

while left < right:
    tmp = num[left] + num[right]
    if tmp == x:
        cnt += 1
        left += 1
    elif tmp < x:
        left += 1
    else:
        right -= 1

print(cnt)