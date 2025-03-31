class Book:
    totalBooks=0
    # adding the book to totalBook
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
        Book.totalBooks+=1

    # updating the title of the book
    def updateTitle(self,newTitle):
        self.title=newTitle

    # updating the author of thebook
    def updateAuthor(self,newAuthor):
        self.author=newAuthor

    # display the book info to user or librarian
    def displayInfo(self,userType="reader"):
        if userType=="librarian":
            print(f"Title of the book:{self.title}, Author of the book:{self.author},ISBN:{self.isbn}")
        else:
            print(f"Title of the book:{self.title}, Author of the book:{self.author}")
    
    @staticmethod       # decorator : it will be directaly associated with class but is notrelated to class object
    def bookInfo():
        print("Books are the foundstion of the education.")
    
    @classmethod
    def getTotalBooks(cls):
        return cls.totalBooks






class Author:
    totalAuthors=0
    def __init__(self,name,birthDate):
        self.name=name
        self.birthDate=birthDate
        self.books=[]
        Author.totalAuthors+=1

    def addBooks(self,book):
        self.book=book
        self.books.append(book)

    def removeBook(self,isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                Book.totalBooks-=1
                print(f"Book with {isbn} removed author named : {self.name} ")
                return print("Book is not available.")
    
    @staticmethod
    def authorInfo():
        print("Author is the content creator.")
    
    @classmethod
    def getTotalAuthors(cls):
        return cls.totalAuthors




class Library:
    libraryCount=0
    def __init__(self):
        self.books=[]
        self.authors=[]
        Library.libraryCount+=1
    
    def addBook(self,book):
        self.books.append(book)

    def removeBook(self,isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                Book.totalBooks-=1
                print(f"Book with {isbn} removed author named : {self.name} ")
                return print("Book is not available.")
    
    def listBooks(self):
        for book in self.books:
            print(f"Title:{book.title}, Author:{book.author},ISBN:{book.isbn}")
    
    @classmethod
    def getLibraryCount(cls):
        return cls.libraryCount
    
    @staticmethod
    def libraryInfo():
        print("Library is access to books and authors.")


book1=Book("Java programming","Vikash","123456")
book2=Book("Python programming","Anchal","234567")

author1=Author("Vikash","2003-04=30")
author1.addBooks(book1)

library=Library()
library.addBook(book1)
library.addBook(book2)

library.listBooks()

book1.updateTitle("Advance Java Programming")
book1.displayInfo("librarian")

print(f"Total Books:{Book.getTotalBooks()}")
print(f"Total Authors:{Author.getTotalAuthors()}")
print(f"Total Libraries:{Library.getLibraryCount()}")

Library.libraryInfo()
Book.bookInfo()
Author.authorInfo()


