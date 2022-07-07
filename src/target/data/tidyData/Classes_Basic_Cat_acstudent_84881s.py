class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        result="name: "+self.name+", age: "+str(self.age)
        return result
    def __str__(self,make_sound):
        make_sound="Meow"
        self.make_sound=make.sound
        return make_sound
c=Cat("Fluffy",3)
