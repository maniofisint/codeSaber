#libray project requires shelves and books
#each book has an id and a name
class library :
    def __init__(self, n_shelves, books_each_sh = 10, books_info = {}):
        self.shelves = []
        for sh in range(n_shelves):
            self.shelves.append(shelf(sh, books_each_sh = 1, books_info = books_info))

    def __str__ (self):
        return 'this is a library'


class shelf :
    def __init__(self, shelf, books_each_sh = 1, books_info = {}):
        self.books = []
        keys = books_info.keys()
        for n in range(books_each_sh) :
            self.books.append(book(shelf, books_info.popitem()))

            

class book :
    def __init__(self, shelf, BUK):
        self.id = BUK[0]
        self.name = BUK[1]
        self.shelf = shelf
        print(shelf,' ',BUK[0],' : ',BUK[1])

booksINF = { '1234' : 'badbadak' ,'2534' : 'nation of love' ,'1323' : 'sadeh'}
library = library(n_shelves = 3, books_each_sh = 2, books_info = booksINF)
