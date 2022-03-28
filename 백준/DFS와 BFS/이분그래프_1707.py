from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    bi[start] = 1
    q = deque()
    q.append(start)
    while q:
        a = q.popleft()
        for i in s[a]:
            if bi[i] == 0:
                bi[i] = -bi[a]
                q.append(i)
            else:
                if bi[i] == bi[a]:
                    return False
    return True

K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    check = 1
    s = [[] for i in range(V + 1)]
    bi = [0 for i in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        s[a].append(b)
        s[b].append(a)
    for i in range(1, V + 1):
        if bi[i] == 0:
            if not bfs(i):
                check = -1
                break
    print("YES"if check == 1 else "NO")