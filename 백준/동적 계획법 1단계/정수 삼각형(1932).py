n = int(input())
tri = []
for _ in range(n):
    tri.append(list(map(int, input().split())))
k = 2
for i in range(1, n):
    for j in range(k):
        if j == 0:
            tri[i][j] += tri[i-1][j]
        elif i == j:
            tri[i][j] += tri[i-1][j-1]
        else:
            tri[i][j] += max(tri[i-1][j], tri[i-1][j-1])
    k += 1
print(max(tri[n-1]))