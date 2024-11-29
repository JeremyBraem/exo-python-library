from sqlalchemy.orm import DeclarativeBase
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from .Base import Base


class BookShop(Base):

    __tablename__ = 'book_bookshop'

    id: Mapped[int] = mapped_column(primary_key=True)
    books: Mapped[List['Book']] = relationship()
    shop_name: Mapped[str] = mapped_column(String())

    def sell_book(self, book):
        if book in self.__books:
            if not book.numeric and book.quantity > 0:
                book.quantity -= 1
                return True
            if book.numeric:
                return True
        return False
