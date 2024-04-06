class Vehicle:
    def __init__(self,m,f):
        self.model = m
        self.fuel_type = f

    model = ""
    fuel_type =""

    def display_info(self):
        return f"{self.model} , {self.fuel_type}"

class Car(Vehicle):
    def __init__(self, m, f):
        super().__init__(m,f)

class Bicycle(Vehicle):
    def __init__(self, m, f, t):
        super().__init__(m, f)
        self.type = t

    type = ""

    def display_info(self):
        return f"Model: {self.model}, Fuel : {self.fuel_type}, Type : {self.type}"

class ElectricCar(Car):
    def __init__(self, m, f):
        super().__init__(m, f)

    doors = 2

    def display_info(self):
        return f"Model : {self.model} , Fuel : {self.fuel_type} , Door : {self.doors} "


class Test:
    i20 = Car("i20","petrol")
    nexon = ElectricCar("Nexon Electric","Electric")
    atlas = Bicycle("Atlas Gold","Manual","Gear")


    print(atlas.display_info())
    print(i20.display_info())
    print(nexon.display_info())


# bacis
class A:
    def show(self):
        print("show from a")

class B(A): 
    def display(self):
        print("display from b")

class Test:
    b = B()
    b.display()
    b.show()
    