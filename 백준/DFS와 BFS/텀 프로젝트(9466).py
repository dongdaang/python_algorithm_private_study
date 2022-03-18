import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

def dfs(i):
    global res
    visited[i] = True
    tmp.append(i)
    
    if visited[nums[i]]:
        if nums[i] in tmp:
            res += tmp[tmp.index(nums[i]):]
        return
    else:
        dfs(nums[i])
        
T = int(input())
for _ in range(T):
    n = int(input())
    nums = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)
    res = []
    for i in range(1, n + 1):
        if visited[i] == False:
            tmp = []
            dfs(i)
    print(n - len(res))