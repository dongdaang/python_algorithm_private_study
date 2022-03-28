from collections import deque

N, K = map(int, input().split())

queue = deque([i for i in range(1, N + 1)])
result = []

while queue:
    i = 0
    while i < K - 1:
        queue.append(queue.popleft())
        i += 1
    result.append(queue.popleft())
print('<', end='')
for i in range(N-1):
    print(result[i], end=', ')
print('{0}>'.format(result[-1]))