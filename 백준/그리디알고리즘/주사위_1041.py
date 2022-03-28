import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
sum=0
sumLists=[]
if(N==1):
    nums = sorted(nums)
    for i in range(0,5):
        sum+=nums[i]
else:
    sumLists.append(min(nums[0],nums[5]))
    sumLists.append(min(nums[1],nums[4]))
    sumLists.append(min(nums[2],nums[3]))
    sumLists = sorted(sumLists)

    min1 = sumLists[0]
    min2 = sumLists[0] + sumLists[1]
    min3 = sumLists[0] + sumLists[1] + sumLists[2]

    n1 = (N-2)*(N-2) + 4*(N-1)*(N-2)
    n2 = 4*(N-2) + 4*(N-1)
    n3 = 4

    sum += n1 * min1
    sum += n2 * min2
    sum += n3 * min3

print(sum)