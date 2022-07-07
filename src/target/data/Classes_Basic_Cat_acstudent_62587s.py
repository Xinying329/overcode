class Cat:
    def __init__(self, name, age):
        self.name=name
        self.age=str(sge)
    def __str__(self):
        return "name: " +self.name+ ", age:" + self.age 
    def make_sound(self):
        return "Meow"
c = Cat("Fluffy", 3)
print(c)
print(c.make_sound())

