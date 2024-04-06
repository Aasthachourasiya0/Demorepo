# object oriented programming


# class A :
     
#      name = "Rajesh"
     
#       # U-D Function
#      def info(self):
#         print("The info is of,", self.name)

# class Test:
# # Object
#     a = A()
# # Function Call
#     a.info()
#     print(a.name)



class Car:
    def __init__(self, make, model, year): #Attributes = make, model, year
        self.make = make
        self.model = model
        self.year = year
    
    def drive(self): #method = drive
        print(f"The {self.make} {self.model} is driving.")

class Test:
    my_car = Car("Toyota", "Corolla", 2022)
    



