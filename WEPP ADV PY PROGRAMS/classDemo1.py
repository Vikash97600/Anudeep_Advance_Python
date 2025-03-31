# WAP to create a Circle class to find the area of circle 
'''
class Circle:
    pi=3.1415

    def __init__(self,radius):
        self.radius=radius

    def area(self):
       return Circle.pi*self.radius**2

circle1=Circle(5)
circle2=Circle(10)

print(f"The value of pi is {circle1.pi}")
print(circle2.pi)
print(f"Area of circle1 is :{circle1.area()}")
print(f"Area of circle2 is :{circle2.area()}")

'''
# WAP to create a rectangle class to find the area of rectangle 

'''
class rectangle:
    def __init__(self,lenght,breadth):
        self.length=lenght
        self.breadth=breadth

    def area(self):
        return self.length*self.breadth 

print(f"The area of rectangle is {rectangle(2,3).area()} meter square")

'''

# WAP to create a class student and find the average marks

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         self.marks={}
#     def addMarks(self,subject,mark):
#         self.marks[subject]=mark
#     def getAvg(self):
#         return sum(self.marks.values())/len(self.marks) if self.marks else 0
#     def displayStu(self):
#         return f"Student:{self.name}, Age:{self.age}, Marks:{self.marks}"  
# student1=Student("vikash",21)

# student1.addMarks("Physics",92)
# student1.addMarks("Math",91)
# student1.addMarks("Python",99)
# print(student1.displayStu())
# print(f"Average marks of the student {student1.name} is : {student1.getAvg()}")



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




