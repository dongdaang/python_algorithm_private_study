from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
queuestack = []
for i in range(N):
    if A[i] == 0:
        queuestack.append(deque([B[i]]))
    else:
        queuestack.append([B[i]])
M = int(input())
C = list(map(int, input().split()))
result = []

for i in C:
    tmp = i
    for j in range(N):
        if A[j] == 0:
            queuestack[j].append(tmp)
            tmp = queuestack[j].popleft()
    result.append(tmp)

for i in result:
    print(i, end=' ')