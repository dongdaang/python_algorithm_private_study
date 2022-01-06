N = int(input())
l = list(map(int, input().split()))
c = list(map(int, input().split()))

total_cost = 0
cost = c[0]
for i in range(N-1):
    if c[i] < cost:
        cost = c[i]
    total_cost += cost * l[i]
print(total_cost)