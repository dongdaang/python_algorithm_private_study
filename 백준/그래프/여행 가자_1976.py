import sys
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    
    if x == y:
        return
    if x > y:
        parent[x] = y
    else:
        parent[y] = x

N = int(input())
M = int(input())
connections = [[0] * (N + 1)]
for _ in range(N):
    connections.append([0] + list(map(int, input().split())))
plan = list(map(int, input().split()))
parent = [i for i in range(N + 1)]
res = 'YES'

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if connections[i][j] == 1:
            union(i, j)

for i in range(len(plan) - 1):
    if parent[plan[i]] != parent[plan[i + 1]]:
        res = 'NO'
        break
print(res)