from dataclasses import dataclass

commands = ["Add book", "Find book", "Remove book", "Find book id", "Stop", "Print all books"]

@dataclass
class Book:
    book_name: str
    author: str
    genre: str
    year_of_publishing: int
    book_id: int

books_list = [
    Book("Book1", "Book author1", "Book genre1", 2015, 1),
    Book("Book2", "Book author2", "Book genre2", 2013, 2),
    Book("Book3", "Book author3", "Book genre3", 0000, 3),
]

def print_book(book):
    print("\nName: {book_name}\nAuthor: {author}\nGenre {genre}\nYear of publishing: {year_of_publishing}\nID: {book_id}".format(book_name=book.book_name, author=book.author,
                                                                                                                                               genre=book.genre, year_of_publishing=book.year_of_publishing, book_id=book.book_id))


class Library():

    def __init__(self):
        self.books = []

    def add_book(self, book_name, author, genre, year_of_publishing):
        id = 0

        if(len(self.books) != 0):
            id = self.books[len(self.books)]

        self.books.append(Book(book_name, author, genre,
                               year_of_publishing, id))

    def add_book_object(self, book):
        self.books.append(book)

    def delete_book(self, book_id):
        for book in self.books:
            if(book.book_id == book_id):
                self.books.remove(book)
                print("Book has benn removed")
                print_book(book)

    def print_all_books(self):
        for book in self.books:
            print_book(book)

    def get_book_by_id(self, id):
        for book in self.books:
            if(book.book_id == id):
                print_book(book)

    def search_book(self, query_dict):

        found_books = []

        for book in self.books:

            if(query_dict['book_name'] == book.book_name or
               query_dict['author'] == book.author or
               query_dict['genre'] == book.genre or
               query_dict['year_of_publishing'] == book.year_of_publishing or
               query_dict['book_id'] == book.book_id):

                found_books.append(book)

        if(len(found_books) == 0):
            print("I can't find this book")
        else:
            for found_book in found_books:
                print_book(found_book)


library = Library()
print("It's Library")
for test_book in books_list:
    library.add_book_object(test_book)

while True:

    print("Commands " + str(commands))
    command = input("Введіть команду: ")

    # Add book
    if command == commands[0]:

        book_name = input("Book name: ")
        author = input("Author: ")
        genre = input("Genre: ")
        year_of_publishing = int(input("Year of publishing: "))

        library.add_book(book_name, author, genre, year_of_publishing)

    # Delete book
    elif command == commands[1]:
        book_id = int(input("Book id: "))
        library.delete_book(book_id)

    # Get book by id
    elif command == commands[2]:
        book_id = input("Book id: ")
        if(book_id != ''):
            library.get_book_by_id(int(book_id))
        else:
            print("Enter book ID")

    # Search
    elif command == commands[3]:
        book_name = input("Book name: ")
        author = input("Author: ")
        genre = input("Genre: ")
        year_of_publishing = input("Year of publishing: ")
        book_id = input("Book id: ")

        if(book_id != ''):
            book_id = int(book_id)

        if(year_of_publishing != ''):
            year_of_publishing = int(year_of_publishing)

        query = {'book_name': book_name, 'author': author, 'genre': genre,
                 'year_of_publishing': year_of_publishing, 'book_id': book_id}
        library.search_book(query)

    # Stop
    elif command == commands[4]:
        print("Bye")
        break

    # Print all books
    elif command == commands[5]:
        library.print_all_books()

    # Print all books
    else:
        library.print_all_books()


def main():
    return 0


if __name__ == '__main__':
    main()
