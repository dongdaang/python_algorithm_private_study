n = int(input())
num = list(map(int, input().split()))

for i in range(2000001):
    for j in num:
        if i % j == 0 and i != j:
            