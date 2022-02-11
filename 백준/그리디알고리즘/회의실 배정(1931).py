import sys
input = sys.stdin.readline

N = int(input())
time = []
for _ in range(N):
    time.append(list(map(int, input().split())))

time.sort(key=lambda x : (x[1], x[0]))

cnt = 1
end = time[0][1]

for i in range(1, N):
    if time[i][0] >= end:
        cnt += 1
        end = time[i][1]

print(cnt)



###################힙 활용 솔루션#################
# import heapq
# import sys
# input = sys.stdin.readline


# N = int(input())
# queue = []
# for _ in range(N):
#     a, b = map(int, input().split())
#     heapq.heappush(queue, (b, a))

# end = 0
# cnt = 0
# for _ in range(N):
#     b, a = heapq.heappop(queue)
#     if a >= end:
#         cnt += 1
#         end = b
        
# print(cnt)