class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return "name: "+self.name+", age: "+self.age
    def make_sound(wrd):
        return "Meow"
c=Cat("Fluffy",3)
