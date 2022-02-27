#############느린 코드############

import sys
input = sys.stdin.readline

L, R = map(int, input().split())
res = str(L).count('8')

while L <= R:
    if '8' in str(L):
        if str(L).count('8') < res:
            res = str(L).count('8')
    else:
        res = 0
        break
    L += 1
print(res)


#############빠른 코드#############

import sys
input = sys.stdin.readline

L, R = input().split()
res = 0

if len(L) == len(R):
  La= list(L)
  Ra = list(R)

  for i in range(0, len(L)):
    if La[i] == Ra[i]:
      if La[i] == '8' and Ra[i] == '8':
        res += 1
    else:
      break

print(res)