from typing import List
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from .Base import Base

class BookCase(Base):

    __tablename__ = 'book_bookcase'

    id: Mapped[int] = mapped_column(primary_key=True)
    books: Mapped[List['Book']] = relationship()

            