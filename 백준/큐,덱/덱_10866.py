import sys
input = sys.stdin.readline

N = int(input())
deque = []

for _ in range(N):
    command = input().strip()

    if command[:6] == 'push_b':
        tmp = command.split(' ')
        deque.append(int(tmp[1]))
    
    elif command[:6] == 'push_f':
        tmp = command.split(' ')
        deque.reverse()
        deque.append(int(tmp[1]))
        deque.reverse()
    
    elif command[:5] == 'pop_f':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
            del(deque[0])
    
    elif command[:5] == 'pop_b':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])
            del(deque[-1])
    
    elif command == 'size':
        print(len(deque))
    
    elif command == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    
    elif command == 'front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])

    elif command == 'back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])