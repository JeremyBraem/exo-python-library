from sqlalchemy.orm import DeclarativeBase
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from .Base import Base


class Book(Base):

    __tablename__ = 'book_book'


    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String())
    author: Mapped[str]= mapped_column(String())
    tags: Mapped[str]= mapped_column(Text())
    numeric: Mapped[bool] = mapped_column(Boolean())
    price: Mapped[int] = mapped_column(Integer())
    quantity: Mapped[int] = mapped_column(Integer())

    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.tags}, {self.numeric}, {self.price}, {self.quantity})"
            
