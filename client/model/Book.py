class Book:
    def __init__(self, title, author, tags, numeric, price, quantity):
        self.__title = title
        self.__author = author
        self.__tags = tags
        self.__numeric = numeric
        self.__price = price
        self.__quantity = quantity

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_title):
        self.__title = new_title

    @property
    def author(self):
        return self.__author
    
    @author.setter
    def author(self, new_author):
        self.__author = new_author

    @property
    def tags(self):
        return self.__tags

    @property
    def numeric(self):
        return self.__numeric
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, new_price):
        self.__price = new_price

    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self, new_quantity):
        self.__quantity = new_quantity

    def add_tag(self, tag):
        self.__tags.append(tag)

    def remove_tag(self, tag):
        if tag in self.tags:
            self.__tags.remove(tag)
            

if __name__ == "__main__":
    books = [
        Book("Book 1", 100, 20, False, 12, 5),
        Book("Book 2", 50, 15, True, 5, 5),
        Book("Book 3", 200, 30, False, 8, 5)
    ]