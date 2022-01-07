import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree = list(map(int, input().split()))

H = max(tree)
while(True):
    sum = 0
    for j in tree:
        if j > H:
            sum += j - H
    if sum < M:
        H -= 1
    else:
        break
print(H)