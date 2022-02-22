import sys, heapq
input = sys.stdin.readline

N = int(input())
leftheap = []
rightheap = []
answer = []
for _ in range(N):
    num = int(input())
    if len(leftheap) == len(rightheap):
        heapq.heappush(leftheap, (-num, num))
    else:
        heapq.heappush(rightheap, (num, num))
    if rightheap and leftheap[0][1] > rightheap[0][0]:
        min = heapq.heappop(rightheap)[0]
        max = heapq.heappop(leftheap)[1]
        heapq.heappush(leftheap, (-min, min))
        heapq.heappush(rightheap, (max, max))
        
    answer.append(leftheap[0][1])
for i in answer:
    print(i)