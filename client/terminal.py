from handler import handle_request
from model.Book import Book
import jsonpickle
def add_book_in_bookshop():
    title = input("Titre: ")
    author = input("Auteur: ")
    tags = input("Liste des tags [tag1,tag2,...]: ")
    is_numeric = input("Livre numérique ? ")
    price = input("Prix unitaire: ")
    quantity = input("Quantité: ")
    book = Book(title, author, tags, is_numeric, price, quantity)
    response = handle_request("add_book_in_bookshop//" + jsonpickle.encode(book))

def display_books():
        print("\n=== Liste des Livres Disponibles ===")
        response = handle_request('display_books//')
        for index, book in enumerate(response):
            print(f"[{index + 1}] Titre: {book.title}, Auteur: {book.author}, "
                  f"Prix: {book.price}€, Quantité: {book.quantity}, Tags: {book.tags}")
        print("====================================\n")

def buy_book():
    book_index = int(input("Entrez le numéro du livre à acheter : ")) - 1
    response = handle_request('buy_book//' + str(book_index))
    print(response)
    return



def exit_program():
     exit(1)

def main():
    actions = {
            "1": display_books,
            "2": buy_book,
            "2a": add_book_in_bookshop,
            "3": exit_program,
        }
    
    while True:
        print("\n=== Menu Principal ===")
        print("1. Afficher les livres")
        print("2. Acheter un livre")
        print("2a. Créer un livre")
        print("3. Quitter")
        print("=======================")
        choix = input("Entrez votre choix : ")

        action = actions.get(choix)
        if action:
            action()  # Appel de la fonction associée
        else:
            print(f"Veuillez sélectionner une option entre 1 et {len(actions.keys())}.")

main()