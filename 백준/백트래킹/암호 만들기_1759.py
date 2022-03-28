import sys
input = sys.stdin.readline

def backtracking(a, pw, consonant_cnt, vowel_cnt):
    if len(pw) == L:
        if consonant_cnt >= 1 and vowel_cnt >= 2:
            res.append(pw)
            return
    for i in range(a, len(letters)):
        if i < a:
            continue
        if letters[i] in consonant:
            backtracking(i + 1, pw + letters[i], consonant_cnt + 1, vowel_cnt)
        else:
            backtracking(i + 1, pw + letters[i], consonant_cnt, vowel_cnt + 1)
        

L, C = map(int, input().split())
letters = list(input().split())
letters.sort()
consonant = ('a', 'e', 'i', 'o', 'u')
consonant_cnt = 0
vowel_cnt = 0
pw = ''
res = []

backtracking(0, pw, consonant_cnt, vowel_cnt)

for password in res:
    print(password)