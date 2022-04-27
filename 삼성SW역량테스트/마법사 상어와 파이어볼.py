N, M, K = map(int, input().split())
fireballs = []
for _ in range(M):
    r, c, m, s, d = list(map(int, input().split()))
    fireballs.append([r - 1, c - 1, m, s, d])

board = [[[] for _ in range(N)] for _ in range(N)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(K):
    while fireballs:
        r, c, m, s, d = fireballs.pop(0)
        nr = (r + s * dx[d]) % N
        nc = (c + s * dy[d]) % N
        board[nr][nc].append([m, s, d])

    for r in range(N):
        for c in range(N):
            if len(board[r][c]) >= 2:
                sum_m, sum_s, cnt_odd, n = 0, 0, 0, len(board[r][c])
                while board[r][c]:
                    _m, _s, _d = board[r][c].pop(0)
                    sum_m += _m
                    sum_s += _s
                    if _d % 2:
                        cnt_odd += 1
                if cnt_odd == n or cnt_odd == 0:
                    nd = [0, 2, 4, 6]
                else:
                    nd = [1, 3, 5, 7]
                if sum_m // 5:
                    for d in nd:
                        fireballs.append([r, c, sum_m // 5, sum_s // n, d])
            if len(board[r][c]) == 1:
                fireballs.append([r, c] + board[r][c].pop())

print(sum([f[2] for f in fireballs]))