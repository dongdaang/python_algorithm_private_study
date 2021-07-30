from user import User

member = {}
my_info = []

menu = input("1. 로그인\n2. 회원가입\n")

if menu == 1:
    id, pw = input('아이디와 비밀번호를 입력해주세요(ex:아이디 비밀번호) : ').split()
    if (id, pw) in member.values():
        a = User(name)
elif menu == 2:
    name = input('이름을 입력해주세요 : ')
    id = input('사용하실 아이디를 입력해주세요 : ')
    pw = input('사용하실 비밀번호를 입력해주세요 : ')
    a = User(name)
    a.add(member, id, pw)