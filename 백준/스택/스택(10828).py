import sys
input = sys.stdin.readline

N = int(input())
s = []
for _ in range(N):
    command = input()
    
    if command[:2] == 'pu':
        s.append(int(command[5:]))
    elif command[:2] == 'po':
        if len(s) == 0:
            print(-1)
        else:
            print(s[-1])
            del(s[-1])
    elif command[0] == 's':
        print(len(s))
    elif command[0] == 'e':
        if len(s) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 't':
        if len(s) == 0:
            print(-1)
        else:
            print(s[-1])




# 정답코드 예시
# import sys

# N = int(sys.stdin.readline())

# stack = []
# rtn = []

# for i in range(N):
#     stack_order = sys.stdin.readline().strip()
#     order = stack_order.split(' ')[0]
    
#     if order == 'push':
#         stack.append(int(stack_order.split(' ')[1]))
        
#     elif order == 'pop':
#         if stack == []:
#             rtn.append(-1)
#         else:
#             rtn.append(stack[-1])
#             stack.pop()
    
#     elif order == 'size':
#         rtn.append(len(stack))
        
#     elif order == 'empty':
#         if stack == []:
#             rtn.append(1)
#         else:
#             rtn.append(0)
            
#     elif order == 'top':
#         if stack == []:
#             rtn.append(-1)
#         else:
#             rtn.append(stack[-1])

# for j in rtn:
#     print(j)