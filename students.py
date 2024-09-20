courses = []
students = []

class Course:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return f"{self.name}"
    

class CourseManager:
    def create(self):
        course = Course(
            input("Enter the name of course: ")
        )
        global courses
        courses.append(course)
        print("Course created!")
    def show_course_by_name(self,name):
        for course in courses:
            if course.name == name:
                return course

    def all_courses(self):
        for course in courses:
            print(course)

    def delete(self,name):
        course = self.show_course_by_name(name)
        courses.remove(course)



class Student:
    id = 0
    def __init__(self,name,surname,age,phone_number,course):
        self.id+=1
        self.name = name
        self.surname = surname
        self.age = age
        self.phone_number = phone_number
        self.course = course
        Student.id+=1

    def __str__(self):
        return f"{self.name} {self.surname} {self.age} {self.phone_number} {self.course}"

class StudenManger:
    def add_student(self):
        student = Student(
            input("Name: "),
            input("Surname: "),
            input("Age: "),
            input("Phone number: "),
            input("Enter the name of course: ")
        )
        global students
        students.append(student)

    def show_student(self,id):
        for student in students:
            if student.id == id:
                return student
    
    def all_students(self,course):
        for student in students:
            if student.course == course:
                print(student)

    def delete_student(self, id):
        student = self.show_student(id)
        students.remove(student)

    

course  = CourseManager()
student = StudenManger()

while True:
    match input("exit, create, all_couses, show_any, delete or admin: "):
        case "create":
            course.create()
        case "all_courses":
            course.all_courses()
        case "show_any":
            a=course.show_course_by_name(input("Enter the name of course to show: "))
            print(a)
        case "delete":
            course.delete(input("Corse name to delete: "))
        case "admin":
            print("You are in admin menu")
            while True:
                user_input = int(input("""1.add student
2.show_student
3.all_students
4.delete_student
5.exit
"""))
                if user_input == 1:
                    student.add_student()
                elif user_input == 2:
                    student1 = student.show_student(int(input("Enter an id: ")))
                    print(student1)
                elif user_input == 3:
                    student.all_students(input("Enter a course: "))
                elif user_input == 4:
                    student.delete_student(int(input("Enter id to delete: ")))
                elif user_input == 5:
                    break
                else:
                    print("From 1 to 5")
        case "exit":
            print("Good bye!")
            break
