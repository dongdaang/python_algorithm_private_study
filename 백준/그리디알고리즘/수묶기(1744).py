import sys
input = sys.stdin.readline

N = int(input())
plus = []
zero = 0
minus = []
result = []
for _ in range(N):
    num = int(input())
    if num == 0:
        zero += 1
    elif num > 0:
        plus.append(num)
    else:
        minus.append(num)
plus.sort()
minus.sort(reverse=True)

while len(minus) > 1:
    a = minus.pop()
    b = minus.pop()
    result.append(a * b)
if len(minus) == 1 and zero == 0:
    result.append(minus.pop())

while len(plus) > 1:
    a = plus.pop()
    b = plus.pop()
    if a == 1 or b == 1:
        result.append(a)
        result.append(b)
    else:
        result.append(a * b)
if len(plus) == 1:
    result.append(plus.pop())
print(sum(result))