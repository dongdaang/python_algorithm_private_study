import sys
sys.setrecursionlimit(10 ** 5)

N, Q = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(2 ** N)]
L = list(map(int, input().split()))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for n in range(Q):
    width = 2 ** L[n]
    for i in range(0, 2 ** N, width):
        for j in range(0, 2 ** N, width):
            tmp = [[0] * width for _ in range(width)]
            now = list(A[k][j:j+width] for k in range(i, i + width))
            for m in range(width):
                for n in range(width):
                    tmp[n][width - m - 1] = now[m][n]
            for m in range(i, i + width):
                for n in range(j, j + width):
                    A[m][n] = tmp[m - i][n - j]

    new_A = list(A[i][:] for i in range(2 ** N))
    for x in range(2 ** N):
        for y in range(2 ** N):
            if not A[x][y]:
                continue
            cnt = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < 2 ** N and 0 <= ny < 2 ** N:
                    if A[nx][ny] > 0:
                        cnt += 1
            if cnt < 3:
                new_A[x][y] -= 1

    A = list(new_A[i][:] for i in range(2 ** N))

res1 = 0
res2 = 0
visited = [[False] * (2 ** N) for _ in range(2 ** N)]

def dfs(x, y):
    global tmp2
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= 2 ** N or ny < 0 or ny >= 2 ** N  or visited[nx][ny] or not A[nx][ny]:
            continue
        tmp2 += 1
        visited[nx][ny] = True
        dfs(nx, ny)

for i in range(2 ** N):
    for j in range(2 ** N):
        if A[i][j] > 0:
            res1 += A[i][j]
            if not visited[i][j]:
                global tmp2
                tmp2 = 0
                dfs(i, j)
                if tmp2 > res2:
                    res2 = tmp2

print(res1)
if res2 == 0:
    print(0)
else:
    print(res2 + 1)