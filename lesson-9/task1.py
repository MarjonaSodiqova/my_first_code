class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
        self.borrow_limit = 3

    def borrow_book(self, book):
        if len(self.borrowed_books) >= self.borrow_limit:
            raise MemberLimitExceededException(f"{self.name} cannot borrow more than {self.borrow_limit} books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"{book.title} is already borrowed.")
        book.is_borrowed = True
        self.borrowed_books.append(book)
        print(f"{self.name} borrowed {book.title}.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}.")
        else:
            print(f"{self.name} did not borrow {book.title}.")

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Added book: {title} by {author}.")

    def add_member(self, name):
        member = Member(name)
        self.members.append(member)
        print(f"Added member: {name}.")

    def borrow_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        book = next((b for b in self.books if b.title == book_title), None)
        
        if not book:
            raise BookNotFoundException(f"Book '{book_title}' not found in the library.")
        if not member:
            print(f"Member '{member_name}' not found.")
            return
        
        member.borrow_book(book)

    def return_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        book = next((b for b in self.books if b.title == book_title), None)
        
        if member and book:
            member.return_book(book)
        else:
            print(f"Invalid return request.")

# Example Usage
def main():
    library = Library()
    library.add_book("1984", "George Orwell")
    library.add_book("To Kill a Mockingbird", "Harper Lee")
    library.add_book("Book 3", "Author Name")  
    library.add_book("Book 4", "Another Author")  
    library.add_member("Alice")
    library.add_member("Bob")
    
    try:
        library.borrow_book("Alice", "1984")
        library.borrow_book("Alice", "1984")  
    except (BookNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException) as e:
        print(e)
    
    try:
        library.borrow_book("Bob", "The Great Gatsby")  
    except BookNotFoundException as e:
        print(e)
    
    try:
        library.borrow_book("Alice", "To Kill a Mockingbird")
        library.borrow_book("Alice", "Book 3") 
        library.borrow_book("Alice", "Book 4")  
    except MemberLimitExceededException as e:
        print(e)
    
    library.return_book("Alice", "1984")
    library.return_book("Bob", "1984")  

if __name__ == "__main__":
    main()
