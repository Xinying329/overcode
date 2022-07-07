import random
random.seed(1)
import pylab
import numpy
class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.make_sound="Meow"
    def __str__(self):
        return "name: "+self.name+" age: "+str(self.age)
    def __make_sound__(self):
        return self.make_sound
c=Cat("Fluffy",3)
