# inheritance helps with code reuseability and we can extend it

class Animal:
    def __init__(self, name, is_alive):
        self.name = name
        self.is_alive = is_alive

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal): #dog inherting from animal  
    def speak(self):
        print(f"{self.name} said wuf")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} said wuf")

class Mouse(Animal):
    def speak(self):
        print(f"{self.name} said wuf")

dog = Dog("Scooby", True)
cat = Cat("Tommy", True)
mouse = Mouse("Jerry", True)


print(dog.name)
cat.sleep()
mouse.eat()
dog.speak()



