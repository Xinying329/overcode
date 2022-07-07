class Cat:
    def __init__(self, name, age):
        self.name
        self.age
        
    def __age__(self):
        return "name: " + self.name + ", " + "age: " + str(self.age) + "."
    
    
c = Cat("Fluffy", 3)
print(c)
print(c.make_sound())

