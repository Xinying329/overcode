class Cat:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        result = "name: " + self.name + ", age: " + str(self.age)
        return result
    
    def __str__(self, make_sound):
        self.make_sound = "Meow"
        return make_sound
        
c = Cat("Fluffy", 3)
print(c)
print(c.make_sound())