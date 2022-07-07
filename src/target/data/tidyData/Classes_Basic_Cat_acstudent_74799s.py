class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return self.name+", "+self.age
c=Cat("Fluffy",3)
