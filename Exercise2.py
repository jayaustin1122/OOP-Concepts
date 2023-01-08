class Student:
    def __init__(self,name,course,year,section):
        self.name = name
        self.course = course
        self.year = year
        self.section = section

    def intro(self):
        print(f"Name    : {self.name}\n"
              f"Course  : {self.course}\n"
              f"Year    : {self.year}\n"
              f"Section : {self.section}")


allStudent = []
while True:
    name = input("Enter Name: ")
    course = input("Enter course: ")
    year = input("Enter year: ")
    section = input("Enter section: ")
    print("")
    student = Student(name,course,year,section)
    allStudent.append(student)
    ask = input("Enter Again [Y/N]")
    if(ask == "Y" ) or (ask =="y"):
        continue
    elif(ask == "N" ) or (ask =="n"):
        print("Thank you")
        break
    else:
        print("Invalid input")
        break
for student in allStudent:
    student.intro()
    print("----------- ")


