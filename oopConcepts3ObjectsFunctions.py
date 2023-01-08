class Animal :
    def __init__(self,type,voice):
        self.type = type
        self.voice = voice

        print(self.type,self.voice)

    def speak (self):
        print(self.voice)

dog = Animal("Dog","arf")
dog.speak()

