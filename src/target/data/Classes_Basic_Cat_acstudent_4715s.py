class Cat:
   def __init__(self,name,age):
       self.name = name
       self.age = age
       #self.make_sound = "Meow"
   def __str__(self):
       return "name: " + self.name + " age: " + str(self.age)
   def make_sound(self):
       return str("Meow")
        
    
c = Cat("Fluffy", 3, "Meow")
print(c)
print(c,make_sound())

