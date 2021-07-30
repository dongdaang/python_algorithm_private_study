N = int(input())

value = []
for i in range(1, N):
    num = []
    for j in range(0, len(str(i))):
        num.append(int(str(i)[j]))
    val = i + sum(num)
    if val == N:
        value.append(i)
if value:
    print(min(value))
if not value:
    print(0)