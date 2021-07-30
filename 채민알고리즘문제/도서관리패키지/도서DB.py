def search(a, t):
    b = [0] * len(a)
    for i in range(len(a)):
        for j in range(5):
            if a[i][j] == t:
                print('\n{0} {1} {2} {3} {4}'.format(a[i][0], a[i][1], a[i][2], a[i][3], a[i][4]))
                b[i] = 1
    if 1 not in b:
        print("\n찾으시는 항목이 없습니다.")

def allbook(a):
    for i in range(len(a)):
        for j in range(5):
            print(a[i][j], end = ' ')
        print('\n')