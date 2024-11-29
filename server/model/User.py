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
from .BookCase import BookCase

class User(Base):

    __tablename__ = 'book_user'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String())
    bookcase: Mapped['BookCase'] = relationship()
    
    def buy_book(self, book_shop, book):
        sell_succeed = book_shop.sell_book(book)
        if sell_succeed:
            self.__bookcase.add_book(book)
            return True