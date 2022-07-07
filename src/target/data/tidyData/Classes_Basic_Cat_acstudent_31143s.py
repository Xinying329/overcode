class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return "name"+" "+name+", age: "+str(age)
c=Cat("Fluffy",3)
