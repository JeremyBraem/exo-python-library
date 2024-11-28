import jsonpickle
from .Book import Book

class BookShop:
    def __init__(self, shop_name = "", books = []):
        self.__shop_name = shop_name
        self.__books = books

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
    
    def save_in_json(self):
        with open("books.json", "w") as f:
            f.write(jsonpickle.encode(self))

    def get_json_file(self): #FIXME: return type BookShop
        book_shop_data = None
        with open("books.json", "r") as f:
            book_shop_data = jsonpickle.decode(f.read())
        self.__shop_name = book_shop_data.shop_name
        self.__books = book_shop_data._BookShop__books
        return book_shop_data

    @classmethod
    def get_json_file_cls(cls): #FIXME: return type BookShop
        book_shop_data = None
        with open("books.json", "r") as f:
            book_shop_data = jsonpickle.decode(f.read(), classes = [Book, BookShop])
        return book_shop_data