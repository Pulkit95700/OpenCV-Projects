# duck typing = concept where the class of an object is less important than the methods/attributes
#               class type is not checked if minimum methods/attributes are present
#               "If it walks like a duck, and quacks like a duch, then it must be a duck"

class Duck:
    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is quacking")

class Chicken:
    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chick is talking")

class Person():
    def catch(self, duck):
        duck.walk()
        duck.talk()

person = Person()
duck = Duck()
chicken = Chicken()

# we can pass both the objects in the person catch method
person.catch(chicken)
# python only examines methods and attributes and more importance is given to these attributes only rather than checking class name