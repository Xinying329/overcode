class Cat:
    def __init__(self,name,age,make_sound):
        self.name=name
        self.age=age
    def __str__(self):
        return "name: "+self.name+" age: "+str(self.age)
    def make_sound():
        return str("Meow")
c=Cat("Fluffy",3)
