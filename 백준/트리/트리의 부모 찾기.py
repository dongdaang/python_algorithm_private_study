# import sys                    시간초과된 코드...

# input = sys.stdin.readline

# def tree(v):
#     for i in range(N + 1):
#         if graph[v][i] == 1 and l[i] == 0:
#             result[i] = v
#             l[i] = 1
#             tree(i)

# N = int(input())
# graph = [[] for _ in range(N + 1)]
# l = [0] * (N + 1)
# l[1] = 1
# result = [0] * (N + 1)

# for _ in range(N-1):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# tree(1)
# for i in range(2, N + 1):
#     print(result[i])

n = int(input())
tree = [[] for i in range(n+1)]

for i in range(n-1):
    a, b = list(map(int, input().split()))
    tree[a].append(b)
    tree[b].append(a)

q = [1]
ans = {}
check = [False for i in range(n+1)]

while len(q) > 0:
    parent = q.pop(0)
    for i in tree[parent]:
        if not check[i]:
            ans[i] = parent
            q.append(i)
            check[i] = True

for i in range(2, n+1):
    print(ans[i])