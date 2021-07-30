print("======== 메뉴 ========\nPUSH : 1\nPOP : 2\nSHOW : 3\n(종료하려면 1,2,3 이외의 수 입력)\n\n")

stack = []

while True:
    menu = int(input("메뉴를 선택하세요 : "))
    if menu == 1:
        num = int(input("수 입력 : "))
        stack.append(num)
    elif menu == 2:
        del(stack[-1])
    elif menu == 3:
        print(stack)
    else:
        break

print("======== 스택 프로그램을 종료합니다. ========")