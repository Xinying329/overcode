class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return "name: "+self.name+" age: "+str(self.age)
    def __make_sound__(self):
        return "Meow"
c=Cat("Fluffy",3)
