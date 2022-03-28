N, M = map(int, input().split())
p = []

def dfs(a):
    if len(p) == M:
        print(' '.join(map(str, p)))
        return
    
    for i in range(a, N+1):
        if i not in p:
            p.append(i)
            dfs(i+1)
            p.pop()
dfs(1)