# Parent Class
class Person:
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
    def introduceSelf(self):
        print(f"Hi i am {self.firstName} {self.lastName}")
# Child Class
class Student(Person):
    def __init__(self,firstName,lastName,sectionYear):# add the additional constructor
        #parent constructor
        super().__init__(firstName,lastName)
        # add attributes
        self.sectionYear = sectionYear

    # overriding functions in python.
    def introduceSelf(self):
        # Changing the contents of the functions
        print(f"Hi i am {self.firstName} {self.lastName} section {self.sectionYear}")

        # overriding and retaining the function content coming from parent Class
        super().introduceSelf()
        print(self.sectionYear)

personOne = Person("Cardo","Dalisay")
personOne.introduceSelf()
studentOne = Student("Miko","Salanca","B")
studentOne.introduceSelf()



