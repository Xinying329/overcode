class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        result="name: "+self.name+", age:"+str(self.age)
        return result
    def __str__(self):
        return
c=Cat("Fluffy",3)
