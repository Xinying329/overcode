class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return "name: " + Cat.name + ", age: " + Cat.age
    def make_sound(self):
        return "Meow"

c = Cat("Fluffy", 3)
print(c)
print(c.make_sound())

