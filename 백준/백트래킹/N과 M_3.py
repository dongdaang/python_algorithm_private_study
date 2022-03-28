N, M = map(int, input().split())

num = []

def f():
    if len(num) == M:
        print(' '.join(map(str, num)))
        return
    
    for i in range(1, N+1):
        num.append(i)
        f()
        num.pop()

f()