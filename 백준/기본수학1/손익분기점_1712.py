A, B, C = map(int, input().split())
if B >= C:
    print("-1")
else:
    cnt = A / (C - B)
    print(int(cnt) + 1)