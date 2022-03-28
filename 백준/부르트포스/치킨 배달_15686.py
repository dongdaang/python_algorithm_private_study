import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
chicken = []
home = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            chicken.append((i, j))
        elif graph[i][j] == 1:
            home.append((i, j))

chicken_not_close = list(combinations(chicken, M))

res = 1000000000
for store in chicken_not_close:
    distance = 0
    for home_location in home:
        min = 101
        for store_location in store:
            tmp = abs(home_location[0] - store_location[0]) + abs(home_location[1] - store_location[1])
            if tmp < min:
                min = tmp
        distance += min
    if distance < res:
        res = distance

print(res)