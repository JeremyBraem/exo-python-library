from model.BookShop import BookShop
from model.Book import Book
from model.Base import Base
import os
import jsonpickle
from sqlalchemy import create_engine

class Application:

    __json_file = "application-bib.json"

    def __init__(self):
        self.reload()
        self.__engine = create_engine('sqlite+pysqlite:///application.db', echo=True)
        Base.metadata.create_all(self.__engine)

    def add_book_in_bookshop(self, book):
        self.__bookshop.add_book(jsonpickle.decode(book))
        self.save_in_json()
        return ('Livre bien ajouté')

    def save_in_json(self):
        with open(self.__json_file, "w") as f:
            f.write(jsonpickle.encode(self))

    def reload(self):
        if not os.path.exists(self.__json_file):
            print(f'Fichier {self.__json_file} introuvable.')
            return False
        with open(self.__json_file, "r") as f:
            application = jsonpickle.decode(f.read(), classes=[Book, BookShop])
            self.__bookshop = application._Application__bookshop
            self.__user = application._Application__user
        return True

    def display_books(self, *args):
        return self.__bookshop.books

    def buy_book(self, book_index):
        book_index = int(book_index)
        try:
            if 0 <= book_index < len(self.__bookshop.books):
                book = self.__bookshop.books[book_index]
                print(book)
                if self.__user.buy_book(self.__bookshop, book):
                    return (f"Vous avez acheté '{book.title}'.")
            else:
                return ("Numéro invalide. Veuillez réessayer.")
        except ValueError:
            return ("Entrée invalide. Veuillez entrer un numéro.")

