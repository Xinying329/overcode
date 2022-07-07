class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self,name,age):
        return "name: "+name+", age: "+str(age)
    def make_sound(self):
        return "Meow"
c=Cat("Fluffy",3)
