#libray project requires shelves and books
#each book has an id and a name
class library :
    def __init__(self,n_shelves,books_each_sh = 10,**books_info) :
        self.shelves = []
        for sh in range(n_shelves) :
            self.shelves.append(shelves(sh,books_each_sh = 1,**books_info))

    def __str__ (self):
        return 'this is a library'


class shelves :
    def __init__(self,shelf,books_each_sh = 1,**books_info):
        self.books = []
        keys = books_info.keys()
        for key in keys:
            for n in range(books_each_sh) :
                self.books.append(books(shelf,key,books_info[key]))
            

class books :
    def __init__(self,shelf,key,books_name):
        self.id = key
        self.name = books_name
        print(shelf,' ',key,' : ',books_name)

books_info = { '1234' : 'badbadak' ,'2534' : 'nation of love' ,'1323' : 'sadeh'}
library = library(n_shelves = 3,books_each_sh = 2,**books_info)