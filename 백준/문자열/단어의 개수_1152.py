s = input()

cnt = 0
for i in range(len(s) - 1):
    if s[i] == ' ' and s[i+1] != ' ':
        cnt += 1

if s[0] == ' ':
    print(cnt)
else:
    print(cnt + 1)


# 정답코드 예시
# import sys
# sentence = sys.stdin.readline().strip()
# if (sentence == ""):
#     print(0)
# else: print(sentence.count(" ") + 1)