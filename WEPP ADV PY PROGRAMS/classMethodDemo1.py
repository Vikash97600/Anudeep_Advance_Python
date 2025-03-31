class User:
    def __init__(self,name, email,user_id):
        self.name=name
        self.email=email
        self.user_id=user_id

    def login(self):
        return f"{self.name} logged in"
            
class Student(User):
    def enroll_course(self, course_name):
        return f"{self.name} enrolled in {course_name}"
    
    def login(self):
        return f"student {self.name} logged in"

class Teacher(User):
    def create_course(self, course_name):
        return f" {self.name} created course {course_name}"

    def login(self):
        return f"Teacher {self.name} logged in"     
    

student = Student('abc','abd@gmail.com', 101)
print(student.login())
print(student.enroll_course('python'))


teacher = Teacher('xyz', 'xyz@gmail.com', 102)
print(teacher.login())
print(teacher.create_course('adv python'))

