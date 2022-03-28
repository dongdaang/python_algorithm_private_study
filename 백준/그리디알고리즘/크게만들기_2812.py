import sys

N,K = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().strip()))

res = []
tmp = K

for i in range(N):
    while tmp > 0 and res:
        if res[-1] < nums[i]:
            res.pop()
            tmp -= 1
        else:
            break
    res.append(nums[i])
    
for i in range(N-K):
    print(res[i], end="")