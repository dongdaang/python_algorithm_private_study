import sys
input = sys.stdin.readline

S = input().rstrip()
target = input().rstrip()

l = len(target)
result = 0
i = 0

while i <= len(S) - l:
    if S[i:i+l] == target:
        result += 1
        S = S[i+l:]
        i = 0
    else:
        i += 1
print(result)