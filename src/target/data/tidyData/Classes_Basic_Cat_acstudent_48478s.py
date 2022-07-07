class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        new_str=""
        new_str+=("name: ",self.name,"age: ",self.age)
        return new_str
c=Cat("Fluffy",3)
