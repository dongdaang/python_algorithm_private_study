N, M = map(int, input().split())

a = min(N, M)
c = 1
for i in range(1, a + 1):
    if N % i == 0 and M % i == 0:
        gcf = i
while(True):
    b = max(N, M) * c
    if b % a == 0:
        lcm = b
        break
    c += 1

print(gcf)
print(lcm)