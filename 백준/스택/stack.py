stack = []
result = []

def push(M):
    M = M.split(' ')
    stack.append(int(M[-1]))

def pop():
    if len(stack) != 0:
        result.append(stack[-1])
        del(stack[-1])
    elif len(stack) == 0:
        result.append(-1)

def size():
    result.append(len(stack))

def empty():
    if len(stack) == 0:
        result.append(1)
    else:
        result.append(0)

def top():
    if len(stack) != 0:
        result.append(stack[-1])
    elif len(stack) == 0:
        result.append(-1)

N = int(input())
for _ in range(N):
    M = input()
    
    if M[:4] == 'push':
        push(M)
    elif M == 'pop':
        pop()
    elif M == 'size':
        size()
    elif M == 'empty':
        empty()
    elif M == 'top':
        top()

for i in result:
    print(i)