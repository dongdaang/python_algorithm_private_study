import repository

def add(a, name, author, year, publisher, genre):
    book_info = []
    book_info.append(name)
    book_info.append(author)
    book_info.append(year)
    book_info.append(publisher)
    book_info.append(genre)
    a.append(book_info)

def edit(a, name, num, c):
    t = 0
    for i in range(len(a)):
        if a[i][0] == name:
            t = i
            break
    if num == 1:
        a[t][0] = c
    elif num == 2:
        a[t][1] = c
    elif num == 3:
        a[t][2] = int(c)
    elif num == 4:
        a[t][3] = c
    else:
        a[t][4] = c

def delete(a, name):
    b = [0] * len(a)
    for i in range(len(a)):
        if a[i][0] == name:
            b[i] = 1
            del(a[i])
            break
    if 1 not in b:
        print("\n해당하는 항목이 존재하지 않습니다.")

def save(a):
    # with open('채민알고리즘문제\도서관리패키지\\input.txt', 'w') as f:
    #     for i in range(len(a)):
    #         for word in a[i]:
    #             a[i][2] = str(a[i][2])
    #             f.write(word)
    #             f.write(' ')
    #         f.write('\n')
    repo = repository.Repository(a)
    repo.update()