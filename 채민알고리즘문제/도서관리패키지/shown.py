def menu_shown():
    num = int(input("\n원하시는 메뉴를 선택해주시오\n\n1. 도서 추가\n2. 도서 검색\n3. 도서 정보 수정\n\
4. 도서 삭제\n5. 현재 총 도서 목록\n6. 저장\n7. 프로그램 나가기(자동 저장)\n"))
    
    return num

def add_shown():
    print("\n추가할 도서 정보를 입력해주시오\n")
    name = input("도서명 : ")
    author = input("저자 : ")
    while True:
        try:
            year = int(input("출판년도 : "))
            break
        except ValueError:
            print("\n잘못된 입력입니다.\n")
            continue
    publisher = input("출판사명 : ")
    genre = input("장르 : ")

    return name, author, year, publisher, genre

def edit_shown():
    name = input("\n정보를 수정할 도서의 이름을 입력해주시오 : ")
    while True:
        try:
            num = int(input("수정할 부분을 선택해주시오 : 1. 도서명  2. 저자  3. 출판년도  4. 출판사명  5. 장르\n"))
            break
        except ValueError:
            print("\n잘못된 입력입니다.\n")
    c = input("수정 내용을 입력해주시오 : ")

    return name, num, c

def delete_shown():
    name = input("\n삭제할 도서명을 입력해주시오 : ")

    return name

def search_shown():
    while True:
        try:
            num = int(input("\n검색 방법을 선택해주시오 : 1. 도서명  2. 저자  3. 출판연도  4. 출판사명  5. 장르"))
            break
        except ValueError:
            print("\n잘못된 입력입니다.\n")
            continue
    if num == 1:
        t = input("도서명을 입력해주시오 : ")
    elif num == 2:
        t = input("저자를 입력해주시오 : ")
    elif num == 3:
        while True:
            try:
                t = int(input("출판연도를 입력해주시오 : "))
                break
            except ValueError:
                print("\n잘못된 입력입니다.\n")
                continue
    elif num == 4:
        t = input("출판사명을 입력해주시오 : ")
    elif num == 5:
        t = input("장르를 입력해주시오 : ")
    return t

def ment(a):
    if a == 1:
        print("\n도서 추가가 완료되었습니다.\n")
    elif a == 2:
        print("\n도서 검색이 완료되었습니다.\n")
    elif a == 3:
        print("\n도서 정보 수정이 완료되었습니다.\n")
    elif a == 4:
        print("\n도서 삭제가 완료되었습니다.\n")
    elif a == 6:
        print("\n저장이 완료되었습니다.\n")
    elif a == 7:
        print("\n프로그램이 종료되었습니다.\n")