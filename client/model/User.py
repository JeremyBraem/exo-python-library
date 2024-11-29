from .BookCase import BookCase

class User:
    def __init__(self, username):
        self.__username = username
        self.__bookcase =  BookCase(username + "_bookcase", [])

    @property
    def username(self):
        return self.__username
    
    def buy_book(self, book_shop, book):
        sell_succeed = book_shop.sell_book(book)
        if sell_succeed:
            self.__bookcase.add_book(book)
            return True