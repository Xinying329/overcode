class Cat:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        result = "name: " + self.name + ", age: " + str(self.age)
        return result
    
    def make_sound:
        c = "Meow"
        return c
        
c = Cat("Fluffy", 3)
print(c)
print(c.make_sound())

