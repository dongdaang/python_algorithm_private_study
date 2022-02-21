import sys
input = sys.stdin.readline

C = int(input())
tmp = 0
for _ in range(C):
    s = input().rstrip()
    a = s.count('for')
    b = s.count('while')
    if a + b > tmp:
        tmp = a + b

print(tmp)