N = int(input())
students = [list(map(int, input().split())) for _ in range(N ** 2)]
seats = [[0] * N for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
res = 0
seats[1][1] = students[0][0]

for i in range(1, N ** 2):
    s, l1, l2, l3, l4 = students[i]
    check_like = [[0] * N for _ in range(N)]
    check_seat = [[0] * N for _ in range(N)]
    flag = True
    like_max = 0
    seat_max = 0

    for x in range(N):
        for y in range(N):
            if seats[x][y] == 0:
                for j in range(4):
                    nx = x + dx[j]
                    ny = y + dy[j]
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue
                    if seats[nx][ny] in (l1, l2, l3, l4):
                        check_like[x][y] += 1
                if check_like[x][y] > like_max:
                    like_max = check_like[x][y]

    for x in range(N):
        for y in range(N):
            if seats[x][y] == 0 and check_like[x][y] == like_max:
                for j in range(4):
                    nx = x + dx[j]
                    ny = y + dy[j]
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue
                    if seats[nx][ny] == 0:
                        check_seat[x][y] += 1
                if check_seat[x][y] > seat_max:
                    seat_max = check_seat[x][y]

    for x in range(N):
        for y in range(N):
            if seats[x][y] == 0:
                if check_like[x][y] == like_max and check_seat[x][y] == seat_max:
                    seats[x][y] = s
                    flag = False
                    break
        if not flag:
            break

while students:
    now = students.pop()
    flag2 = True
    for x in range(N):
        for y in range(N):
            if seats[x][y] == now[0]:
                cnt = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue
                    if seats[nx][ny] in now[1:]:
                        cnt += 1
                if cnt > 0:
                    res += 10 ** (cnt - 1)
                flag2 = False
                break
        if not flag2:
            break

print(res)