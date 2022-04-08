import sys
input = sys.stdin.readline

N = int(input())
dp_max = [0] * 3
dp_min = [0] * 3
for _ in range(N):
    scores = list(map(int, input().split()))
    dp_tmp = dp_max[:]
    dp_tmp[0] = max(dp_max[0], dp_max[1]) + scores[0]
    dp_tmp[1] = max(dp_max[0], dp_max[1], dp_max[2]) + scores[1]
    dp_tmp[2] = max(dp_max[1], dp_max[2]) + scores[2]
    dp_max = dp_tmp[:]
    dp_tmp = dp_min[:]
    dp_tmp[0] = min(dp_min[0], dp_min[1]) + scores[0]
    dp_tmp[1] = min(dp_min[0], dp_min[1], dp_min[2]) + scores[1]
    dp_tmp[2] = min(dp_min[1], dp_min[2]) + scores[2]
    dp_min = dp_tmp[:]
print(max(dp_max), min(dp_min))