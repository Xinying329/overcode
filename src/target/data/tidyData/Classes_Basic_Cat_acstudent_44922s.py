class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return 'name: '+self.age+', age: '+str(self.age)
    def make_sound(self):
        return "Meow"
c=Cat("Fluffy",3)
