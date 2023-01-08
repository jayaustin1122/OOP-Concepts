class User :
    def __init__(self,firstName,lastName,likesCount,friendsName):
        self.firstName = firstName
        self.lastName = lastName
        self.likesCount = int(likesCount)
        self.friendsName = friendsName

    def introduceSelf(self):
        print(f"Hi i am {self.firstName} {self.lastName}")

    def showAllDetails(self):
        print(f"Fullname: {self.firstName} {self.lastName}\n"
              f"Likes: {self.likesCount}\n"
              f"Friends: ")
        for i in self.friendsName:
            print(i)





user = User("Cardo","Dalisay",10,["pogi","cardo1"])
user.introduceSelf()
user.showAllDetails()