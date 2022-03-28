import sys
input = sys.stdin.readline

N = int(input())
words = []
nums = {}
for _ in range(N):
    words.append(input().rstrip())

for word in words:
    for i in range(len(word)):
        if word[i] not in nums:
            nums[word[i]] = 10 ** (len(word) - i - 1)
        else:
            nums[word[i]] += 10 ** (len(word) - i - 1)
            
current = 9
res = 0

point = list(nums.values())
point.sort(reverse=True)
for i in point:
    res += current * i
    current -= 1

print(res)