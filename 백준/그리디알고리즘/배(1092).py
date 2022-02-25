import sys
input = sys.stdin.readline

N = int(input())
cranes = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

if boxes[0] > cranes[0]:
    print(-1)
else:
    time = 0
    while boxes:
        for i in cranes:
            for j in boxes:
                if i >= j:
                    boxes.remove(j)
                    break
        time += 1
    print(time)