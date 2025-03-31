class Library:
    # Class attributes
    total_books = 5
    all_books = ["The Great Gatsby", "1984", "Moby Dick", "War and Peace", "Hamlet"]

    def __init__(self, name):
        # Instance attributes
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        # Check if the book is available
        if book in Library.all_books:
            Library.all_books.remove(book)  # Remove the book from the library
            self.borrowed_books.append(book)  # Add it to the member's borrowed list
            Library.total_books -= 1  # Decrease the total number of books
            return f"{self.name} borrowed '{book}'"
        else:
            return "Book not available"

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)  # Remove it from the member's borrowed list
            Library.all_books.append(book)  # Add it back to the library
            Library.total_books += 1  # Increase the total number of books
            return f"{self.name} returned '{book}'"
        else:
            return f"{self.name} hasn't borrowed '{book}'"

    @classmethod
    def view_library_books(cls):
        print(f"Total books in the library: {cls.total_books}")
        print("Available books:", cls.all_books)

# Example usage:
# Creating a library member
member = Library("Alice")

# Borrowing a book
print(member.borrow_book("The Great Gatsby"))  # Output: Alice borrowed 'The Great Gatsby'

# Viewing available books in the library
Library.view_library_books()

# Returning a book
print(member.return_book("The Great Gatsby"))  # Output: Alice returned 'The Great Gatsby'

# Viewing available books after returning
Library.view_library_books()