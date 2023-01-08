class Person :
    #constructor
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("My name is "+name+" i am "+str(age)+" years old")

person = Person("Cardo",21)
