N, M = map(int, input().split())
num = list(map(int, input().split()))
value = []
for i in range(0,N-2):
    for j in range(i+1,N-1):
        for k in range(j+1, N):
            val = num[i] + num[j] + num[k]
            if val <= M:
                value.append(val)
print(max(value))