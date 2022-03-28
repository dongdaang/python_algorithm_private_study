import sys
input = sys.stdin.readline

N = int(input())
weights = list(map(int, input().split()))
weights.sort()
total = 0
for i in range(N):
    if total + 1 >= weights[i] :
        total += weights[i]
    else:
        break

print(total + 1)