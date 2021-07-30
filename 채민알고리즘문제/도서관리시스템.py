from 도서관리패키지.shown import menu_shown, add_shown, edit_shown, delete_shown, search_shown, ment
from 도서관리패키지.도서관리 import add, edit, delete, save
from 도서관리패키지.도서DB import search, allbook

book_list = []

with open('채민알고리즘문제\도서관리패키지\input.txt', 'r') as file:
    for text in file:
        book_list.append(text.strip().split(' '))
        print(text.strip('\n'))
for i in range(len(book_list)):
    book_list[i][2] = int(book_list[i][2])

while True:
    try:
        num = menu_shown()
    except ValueError:
        print("\n잘못된 입력입니다.\n")
        continue

    if num == 1:
        name, author, year, publisher, genre = add_shown()
        add(book_list, name, author, year, publisher, genre)
        ment(num)
    elif num == 2:
        t = search_shown()
        search(book_list, t)
        ment(num)
    elif num == 3:
        name, num_2, c = edit_shown()
        edit(book_list, name, num_2, c)
        ment(num)
    elif num == 4:
        name = delete_shown()
        delete(book_list, name)
        ment(num)
    elif num == 5:
        allbook(book_list)
    elif num == 6:
        save(book_list)
        ment(num)
    elif num == 7:
        save(book_list)
        ment(num)
        break