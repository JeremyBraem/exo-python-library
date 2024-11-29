class BookShop:
    def __init__(self, shop_name="", books=None):
        self.__shop_name = shop_name
        if books:
            self.__books = books
        else:
            self.__books = []

    @property
    def books(self):
        return self.__books.copy()

    @property
    def shop_name(self):
        return self.__shop_name

    @shop_name.setter
    def shop_name(self, value):
        self.__shop_name = value

    def add_book(self, book):
        self.__books.append(book)

    def sell_book(self, book):
        if not book.numeric and book in self.__books and book.quantity > 0:
            self.__books.remove(book)
            book.quantity -= 1
            return True
        return False
