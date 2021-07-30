class User:
    def __init__(self, name):
        self.name = name

    def add(self, member, id, pw):
        member[self.name] = (id, pw)

    def log_in():
        pass

    def mypage(self, my_info, name):
        for i in range(len(my_info)):
            if my_info[i][0] == name:
                for j in range(len(my_info[i])):
                    print(my_info[i][j], end = ' ')