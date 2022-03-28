import sys
input = sys.stdin.readline

N, M = map(int, input().split())
books = list(map(int, input().split()))
books.sort()
books = [abs(i) for i in books]

res = 0
l, r = 0, len(books) - 1
if sum(books[:M]) > sum(books[:-M-1]):
    res += books[l]
    l += M
else:
    res += books[r]
    r -= M
while l <= r:
    if (books[l] < 0 and books[l+1] > 0) or (books[r-1] < 0 and books[r] > 0):
        pass
    elif sum(books[l:l+M]) > sum(books[r-(M-1):r+(M-1)]):
        res += books[l] * 2
        l += M
    else:
        res += books[r] * 2
        r -= M
print(books)