#실제 DB에 접근하는 Class
class Repository():
    def __init__(self, book_list):
        self.book_list = book_list

    def read(self):
        with open('채민알고리즘문제\도서관리패키지\input.txt', 'r') as file:
            for text in file:
                self.book_list.append(text.strip().split(' '))
                print(text.strip('\n'))
            for i in range(len(self.book_list)):
                self.book_list[i][2] = int(self.book_list[i][2])
    def update(self):
        with open('채민알고리즘문제\도서관리패키지\\input.txt', 'w') as f:
            for i in range(len(self.book_list)):
                for word in self.book_list[i]:
                    self.book_list[i][2] = str(self.book_list[i][2])
                    f.write(word)
                    f.write(' ')
                f.write('\n')




