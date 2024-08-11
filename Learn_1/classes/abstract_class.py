# Abstract classes and methods in python
# + compels a user to override abstract methods in a child class
# abstract_class = a class which contains one or more abstract methods
# abstract_method = a method that has a declaration but does not have an implementation

# its like a ghost class

from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You ride a car")

class Motorcycle(Vehicle):
    def go(self):
        print("You ride a motorcycle")

vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

# we need at least one abstract method in abstract class. Hence if there are no abstract methods in an abstract class it can be instantiated.
vehicle.go()
car.go()
# Traceback (most recent call last):
#   File "D:\python\Learn_1\classes\abstract_class.py", line 22, in <module>
#     vehicle = Vehicle()
#               ^^^^^^^^^
# TypeError: Can't instantiate abstract class Vehicle without an implementation for abstract method 'go'
motorcycle.go()

# abstract class wo class hoti jo ki implement to ho sakti hai par uska object nahi bana sakte. Use bas inherit karte hain.
# agar kisi abstract class main koi koi abstract method nhi hai to apan us class ka object bana sakte hain par agar abstract
# method hai to fir apan us class ka object nhi bana sakte hain.
# to agar maan lo kisi aur class ne apni abstract class ko inherit kiya to ab kya hoga ki abstract class ke methods us class main inherit
# ho jaayenge to fir apan un child classes ko bhi instantiate nahi kar sakte haina, to kya kareign agar inhe instantiate karna hai to
# simple method overriding ki madad se upar wale abstract method ko override kardo is se upar wale method jo ki abstract method that wo
# ab simple method ban jaayega aur kyunki tumhari class main koi abstract method nahi hai to fir use tum instantiate kar sakte ho.