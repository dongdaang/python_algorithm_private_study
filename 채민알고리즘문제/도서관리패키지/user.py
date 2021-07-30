import menu

book_list = []

user = bookServer.Book(book_list)

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