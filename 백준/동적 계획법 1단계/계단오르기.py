N = int(input())

s = [0 for i in range(300)]
d = [0 for i in range(300)]

for i in range(N):
    s[i] = int(input())

d[0] = s[0]
d[1] = s[0] + s[i]
d[2] = max(s[0] + s[2], s[1] + s[2])

for i in range(3, N):
    d[i] = max(d[i-3] + s[i-1] + s[i], d[i-2] + s[i])
print(d[N-1])