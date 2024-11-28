import jsonpickle

class BookShop : 
    def __init__(self, shop_name, books):
        self.shop_name = shop_name
        self.books = books

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
        with open("books.json", "a") as f:
            f.write(jsonpickle.encode(self))

    def get_json_file(self):
        book_shop_data = None
        with open("books.json", "r") as f:
            book_shop_data = jsonpickle.decode(f.read)
            
        return book_shop_data


            