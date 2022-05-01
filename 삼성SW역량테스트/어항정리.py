def control(a):
    grid = [[0] * 100 for _ in range(100)]
    new_grid = [[0] * 100  for _ in range(100)]
    check_grid = [[False] * 100 for _ in range(100)]
    for i in range(len(a)):
        for j in range(99, 99 - len(a[i]), -1):
            grid[j][i] = a[i][99 - j]
            check_grid[j][i] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(len(a)):
        for j in range(99, 99 - len(a[i]), -1):
            for k in range(4):
                nx = j + dx[k]
                ny = i + dy[k]
                if nx <= 99 - len(a[i]) or nx >= 100 or ny < 0 or ny >= len(a) or not check_grid[nx][ny]:
                    continue
                diff = grid[j][i] - grid[nx][ny]
                if diff > 0:
                    d = diff // 5
                    if d > 0:
                        new_grid[j][i] -= d
                        new_grid[nx][ny] += d

    for i in range(100):
        for j in range(100):
            grid[i][j] += new_grid[i][j]

    for i in range(len(fishbowl)):
        for j in range(99, 99 - len(a[i]), -1):
            a[i][99 - j] = grid[j][i]

    return a

N, K = map(int, input().split())
fishbowl = [[] for _ in range(N)]
fish = list(map(int, input().split()))
for i in range(N):
    fishbowl[i].append(fish[i])

m = 10001
for i in range(N):
    tmp = fishbowl[i][0]
    if tmp < m:
        m = tmp

for i in range(N):
    if fishbowl[i][0] == m:
        fishbowl[i][0] += 1

current_bowl = fishbowl.pop(0)
for i in range(len(current_bowl)):
    fishbowl[i].append(current_bowl[i])

while True:
    tmp = []
    while len(fishbowl[0]) >= 2:
        tmp.append(fishbowl.pop(0))

    if len(tmp[0]) > len(fishbowl):
        fishbowl = tmp + fishbowl
        break

    while tmp:
        now = tmp.pop()
        for i in range(len(now)):
            fishbowl[i].append(now[i])

fishbowl = control(fishbowl)
new_fishbowl = []
for i in fishbowl:
    new_fishbowl += i

tmp1 = new_fishbowl[:N // 2]
tmp1.reverse()
tmp2 = new_fishbowl[N // 2:]

tmp3 = tmp1[:N // 4]
tmp3.reverse()
tmp4 = tmp1[N // 4:]
tmp5 = tmp2[:N // 4]
tmp5.reverse()
tmp6 = tmp2[N // 4:]

new_fishbowl_2 = []
for j in range(len(tmp3)):
    b = []
    b.append(tmp6[j])
    b.append(tmp4[j])
    b.append(tmp3[j])
    b.append(tmp5[j])
    new_fishbowl_2.append(b)

# print(new_fishbowl_2)
new_fishbowl_2 = control(new_fishbowl_2)

print(new_fishbowl_2)