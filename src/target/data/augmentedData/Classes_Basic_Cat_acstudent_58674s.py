import random
random.seed(1)
import pylab
import numpy
class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        result="name: "+self.name+", age: "+str(self.age)
        return result
    def make_sound(self):
        return "Meow"
c=Cat("Fluffy",3)
