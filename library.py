class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

class LibraryMember:
    def __init__(self, name):
        self.name = name
        self._borrowed_books = []

    def borrow_book(self, book):
        if len(self._borrowed_books) < self.borrow_limit() and book.is_available:
            self._borrowed_books.append(book)
            book.is_available = False
            return True
        return False

    def return_book(self, book):
        if book in self._borrowed_books:
            self._borrowed_books.remove(book)
            book.is_available = True
            return True
        return False

    def borrow_limit(self):
        return 0

class StudentMember(LibraryMember):
    def __init__(self, name):
        super().__init__(name)
    def borrow_limit(self):
        return 2

class TeacherMember(LibraryMember):
    def __init__(self, name):
        super().__init__(name)
    def borrow_limit(self):
        return 5

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, member, book):
        if book in self.books and book.is_available:
            if member.borrow_book(book):
                return f"{member.name} borrowed '{book.title}'"
            else:
                return "Borrowing limit reached"
        return "Book not available"

    def return_book(self, member, book):
        if book in self.books and member in self.members:
            if member.return_book(book):
                return f"{member.name} returned '{book.title}'"
            else:
                return "Book was not borrowed by this member"
        return "Invalid member or book"

if __name__ == "__main__":
    library = Library()

    books = [
        Book("Python Crash Course", "Eric Matthes"),
        Book("Head First Python", "Paul Barry"),
        Book("Automate the Boring Stuff with Python", "Al Sweigart"),
        Book("Fluent Python", "Luciano Ramalho"),
        Book("Effective Python", "Brett Slatkin"),
        Book("Programming Python", "Mark Lutz")
    ]
    for book in books:
        library.add_book(book)

    student = StudentMember("Emre")
    teacher = TeacherMember("Mr.Bhuiyan")
    library.add_member(student)
    library.add_member(teacher)

    print(library.borrow_book(student, books[0]))
    print(library.borrow_book(student, books[1]))
    print(library.borrow_book(student, books[2]))

    print(library.borrow_book(teacher, books[2]))
    print(library.borrow_book(teacher, books[3]))
    print(library.borrow_book(teacher, books[4]))
    print(library.borrow_book(teacher, books[5]))
    print(library.borrow_book(teacher, books[0]))
    print(library.borrow_book(teacher, books[2]))

    print(library.return_book(student, books[0]))
    print(library.borrow_book(teacher, books[0]))