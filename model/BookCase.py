class BookCase:
    def __init__(self, id, books = None):
        self.__id = id
        if books:
            self.__books = books
        else:
            self.__books = list()

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value):
        self.__id = value

    def add_book(self, book):
        self.__books.append(book)

            