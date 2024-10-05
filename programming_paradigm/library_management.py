class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False

    def check_book_out(self):
        self.__is_checked_out = True
        return self.__is_checked_out


    def return_book(self):
        self.__is_checked_out = False
        return self.__is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self.__books = []
        self.__checked_out_books = []

    def add_book(self, book):
        self.__books.append(book)

    def check_out_book(self, title):
            for book in self.__books:
                if book.title == title:
                    self.__books.remove(book)
                    self.__checked_out_books.append(book)
                    break

    def return_book(self, title):
        for book in self.__checked_out_books:
            if book.title == title:
                self.__books.append(book)
                self.__checked_out_books.remove(book)
                break


    def list_available_books(self):
        for book in self.__books:
            print(book)

        