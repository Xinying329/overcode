class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
    
    
c = Cat("Fluffy", 3)
print(c)
print(c.make_sound())

