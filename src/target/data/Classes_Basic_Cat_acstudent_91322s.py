class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        self.name = str(self.name)
        self.age = str(self.age)
        return "name: " + self.name + " , age: " + self.age
    def make_sound(self):
        return "Meow"

c = Cat("Fluffy", 3)
print(c)
print(c.make_sound())

