import repository

class Book():
    def __init__(self, book_info):
        self.book_info = book_info

    def add(self, name, author, year, publisher, genre):
        self.book_info = []
        self.book_info.append(name)
        self.book_info.append(author)
        self.book_info.append(year)
        self.book_info.append(publisher)
        self.book_info.append(genre)

    def edit(self, name, num, c):
        t = 0
        for i in range(len(self.book_info)):
            if self.book_info[i][0] == name:
                t = i
                break
        if num == 1:
            self.book_info[t][0] = c
        elif num == 2:
            self.book_info[t][1] = c
        elif num == 3:
            self.book_info[t][2] = int(c)
        elif num == 4:
            self.book_info[t][3] = c
        else:
            self.book_info[t][4] = c 

    def delete(self, name):
        b = [0] * len(self.book_info)
        for i in range(len(self.book_info)):
            if self.book_info[i][0] == name:
                b[i] = 1
                del(self.book_info[i])
                break
        if 1 not in b:
            print("\n해당하는 항목이 존재하지 않습니다.")   

    def save(self):
        repo = repository.Repository(self.book_info)
        repo.update()
    
    def search(self, t):
        b = [0] * len(self.book_info)
        for i in range(len(self.book_info)):
            for j in range(5):
                if self.book_info[i][j] == t:
                    print('\n{0} {1} {2} {3} {4}'.format(self.book_info[i][0], self.book_info[i][1], self.book_info[i][2], self.book_info[i][3], self.book_info[i][4]))
                    b[i] = 1
        if 1 not in b:
            print("\n찾으시는 항목이 없습니다.")

    def allbook(self):
        for i in range(len(self.book_info)):
            for j in range(5):
                print(self.book_info[i][j], end = ' ')
            print('\n')