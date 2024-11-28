from classes.BookShop import BookShop
from classes.User import User
class Application:
    def __init__(self):
        self.__users = []
        self.__bookshop = BookShop()

    #FIXME save in json with pickle
    def save(self):
        pass

    def reload(self):
        pass

    def display_books(self, books):
        print("\n=== Liste des Livres Disponibles ===")
        for index, book in enumerate(books):
            print(f"[{index + 1}] Titre: {book.title}, Auteur: {book.author}, "
                f"Prix: {book.price}€, Quantité: {book.quantity}, Tags: {book.tags}")
        print("====================================\n")

    def main(self):
        book_shop = BookShop.get_json_file_cls()
        user = User("Oui")
        while True:
            print("\n=== Menu Principal ===")
            print("1. Afficher les livres")
            print("2. Acheter un livre")
            print("3. Enregistrer la librairie")
            print("4. Recharger la librairie")
            print("5. Quitter")
            print("=======================")
            choix = input("Entrez votre choix : ")

            if choix == "1":
                self.display_books(book_shop._BookShop__books)

            elif choix == "2":
                self.display_books(book_shop._BookShop__books)
                book_index = int(input("Entrez le numéro du livre à acheter : ")) - 1
                if 0 <= book_index < len(book_shop._BookShop__books):
                    book = book_shop._BookShop__books[book_index]
                    if user.buy_book(book_shop, book):
                        print(f"Vous avez acheté '{book.title}'.")
            elif choix == "3":
                book_shop.save_in_json()
                print("Librairie enregistrée dans 'books.json'.")

            elif choix == "4":
                book_shop = BookShop.get_json_file_cls()
                print(book_shop)
                print("Librairie rechargée depuis 'books.json'.")

            elif choix == "5":
                print("À bientôt !")
                break

            else:
                print("Veuillez sélectionner une option entre 1 et 5.")

if __name__ == "__main__":
    Application().main()