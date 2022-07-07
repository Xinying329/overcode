class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        new_str=""
        new_str+="name: "
        new_str+=self.name+" "
        new_str+="age: "
        new_str+=str(self.age)
        return new_str
    def make_sound(self):
        return "Meow"
c=Cat("Fluffy",3)
