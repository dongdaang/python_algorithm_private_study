N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
r, c = N // 2, N // 2
res = 0
left_case = [(-1, 0), (1, 0), (-1, -1), (1, -1), (-2, -1), (2, -1), (-1, -2), (1, -2), (0 ,-3)]
down_case = [(0, -1), (0, 1), (1, -1), (1, 1), (1, -2), (1, 2), (2, -1), (2, 1), (3, 0)]
right_case = [(-1, 0), (1, 0), (-1, 1), (1, 1), (-2, 1), (2, 1), (-1, 2), (1, 2), (0, 3)]
up_case = [(0, -1), (0, 1), (-1, -1), (-1, 1), (-1, -2), (-1, 2), (-2, -1), (-2, 1), (-3, 0)]
rate = [0.01, 0.01, 0.07, 0.07, 0.02, 0.02, 0.1, 0.1, 0.05]
flag = 0
step = 1
while True:
    if flag == 0:
        for _ in range(step):
            tmp = 0
            for i in range(9):
                dr, dc = left_case[i]
                nr, nc = r + dr, c + dc
                sand = int(A[r][c - 1] * rate[i])
                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    res += sand
                    tmp += sand
                else:
                    A[nr][nc] += sand
                    tmp += sand
            if c - 2 >= 0:
                A[r][c - 2] += A[r][c - 1] - tmp
            else:
                res += A[r][c - 1] - tmp
            A[r][c - 1] = 0
            c -= 1
            if (r, c) == (0, 0):
                break
        if (r, c) == (0, 0):
            break
        for _ in range(step):
            tmp = 0
            for i in range(9):
                dr, dc = down_case[i]
                nr, nc = r + dr, c + dc
                sand = int(A[r + 1][c] * rate[i])
                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    res += sand
                    tmp += sand
                else:
                    A[nr][nc] += sand
                    tmp += sand
            if r + 2 < N:
                A[r + 2][c] += A[r + 1][c] - tmp
            else:
                res += A[r + 1][c] - tmp
            A[r + 1][c] = 0
            r += 1
        step += 1
        flag = 1
    else:
        for _ in range(step):
            tmp = 0
            for i in range(9):
                dr, dc = right_case[i]
                nr, nc = r + dr, c + dc
                sand = int(A[r][c + 1] * rate[i])
                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    res += sand
                    tmp += sand
                else:
                    A[nr][nc] += sand
                    tmp += sand
            if c + 2 < N:
                A[r][c + 2] += A[r][c + 1] - tmp
            else:
                res += A[r][c + 1] - tmp
            A[r][c + 1] = 0
            c += 1
        for _ in range(step):
            tmp = 0
            for i in range(9):
                dr, dc = up_case[i]
                nr, nc = r + dr, c + dc
                sand = int(A[r - 1][c] * rate[i])
                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    res += sand
                    tmp += sand
                else:
                    A[nr][nc] += sand
                    tmp += sand
            if r - 2 >= 0:
                A[r - 2][c] += A[r - 1][c] - tmp
            else:
                res += A[r - 1][c] - tmp
            A[r - 1][c] = 0
            r -= 1
        step += 1
        flag = 0

print(res)