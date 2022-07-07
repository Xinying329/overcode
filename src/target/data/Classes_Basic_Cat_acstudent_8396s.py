
class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=int(age)
    def __str__(self):
        return ("name: " + self.name + " " + "age: " + int(self.age))
    def make_sound(self):
        return "Meow"

c = Cat("Fluffy", 3)
print(c)
print(c.make_sound())

