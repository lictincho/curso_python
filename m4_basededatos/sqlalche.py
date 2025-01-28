from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.sql import exists

# crea base de datos en memoria
engine = create_engine('sqlite:///:memory:')
Base = declarative_base()

# crea clase para definir la tabla y las columnas
class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, Sequence('author_id_seq'), primary_key=True)
    firstname = Column(String)
    lastname = Column(String)

    books = relationship("Book", order_by="Book.id", back_populates="author")

    def __repr__(self):
        return f"{self.firstname} {self.lastname}"


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, Sequence('book_id_seq'), primary_key=True)
    isbn = Column(String)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('author.id'))
    
    author = relationship("Author", back_populates="books")

    def __repr__(self):
        return f"{self.title}"


Base.metadata.create_all(engine)

# inicia una sesión
Session = sessionmaker(bind=engine)
session = Session()

#Agregando a la tabla
author1 = Author(firstname='firstname1', lastname='lastname1')

author2 = Author(firstname='firstname2', lastname='lastname2')
author2.books = [Book (isbn="isbn1",
                 title="title1"),
            Book(isbn="isbn3",
                 title="title3")]

author3 = Author(firstname='firstname3', lastname='lastname3')
author3.books = [Book (isbn="isbn2",
                 title="title2")]

session.add(author1)
session.add(author2)
session.add(author3)

# cierra sesion y guarda en la basa de datos
session.commit()

print("Respuesta:")
print(session.query(Author.firstname).filter(Author.books.any()).count())

