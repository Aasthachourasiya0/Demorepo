# from abc import ABC , abstractmethod

# class A(ABC):
#     @abstractmethod
#     def run(self):
#         pass

# class B(A):
#     def run(self):
#         print("run from c")

# class C(A):
#     def run(self):
#         print("run from c")


# class Test:
#     a = A()
#     b = B()
#     c = C()

#     a.run()
#     b.run()
#     c.run()


from abc import ABC , abstractmethod

class Car (ABC):
    @abstractmethod
    def engine(self):
        pass

    @abstractmethod
    def body(self):
        pass

    @abstractmethod
    def controls(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass

class Honda(Car):
    def engine(self):
        return "DOHC"
    
    def body(self):
        return "sendan"
    
    def controls(self):
        return "Autometic"
    
    def fuel_type(self):
        return "Petrol"

class Test:
    civic = Honda()
    print("The Engine Civic has is :",civic.engine())
    print("The Controls Civic has is :",civic.controls())
    print("The Body Civic has is :",civic.body())
    print("The Fuel Type Civic has is :",civic.fuel_type())
    
