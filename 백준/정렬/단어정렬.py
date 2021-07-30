import sys

N = int(input())

words = []

for _ in range(N):
    words.append(sys.stdin.readline().rstrip())
words = list(set(words))

new_words = []

for i in words:
    new_words.append((len(i), i))

result = sorted(new_words)

for i, j in result:
    print(j)