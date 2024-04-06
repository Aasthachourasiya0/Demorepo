

class UserDetails:
    __username = ""
    __password = ""

    def setUsername(self,u):
        self.__username = u
        
    def setPassword(self,p):
        self.__password = p

    def getUsername(self):
        return self.__username
    

class App:
    user1 = UserDetails()
    user2 = UserDetails()

    user1.setUsername("rajesh")
    user1.setPassword("1234")
    print("The Username of User 1 is :",user1.getUsername())
    print("The password of User 1 is :",user1.getpasswword())


 
