class Cat:
    def __init__(self,name,age):
        self.name=str(name)
        self.age=age
    def __str__(self):
        return "name:"+self.name and "age:"+self.age
    def make_sound(self):
        return "Meow"
c=Cat("Fluffy",3)
