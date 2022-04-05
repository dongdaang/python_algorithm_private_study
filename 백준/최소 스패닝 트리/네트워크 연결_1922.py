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
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

N = int(input())
M = int(input())
network = []
for _ in range(M):
    a, b, c = map(int, input().split())
    network.append((c, a, b))
network.sort()
parent = [i for i in range(N + 1)]
res = 0

for i in range(M):
    if find(network[i][1]) == find(network[i][2]):
        continue
    res += network[i][0]
    union(network[i][1], network[i][2])

print(res)