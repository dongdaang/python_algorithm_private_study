from collections import deque

queue = deque([[1, 2]])
a, b = queue.popleft()
print(a)