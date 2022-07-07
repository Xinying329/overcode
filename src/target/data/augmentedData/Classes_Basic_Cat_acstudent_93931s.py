import random
random.seed(1)
import pylab
import numpy
c=Cat("Fluffy",3)
class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return "name: "+self.name+", age: "+self.age
    def make_sound(wrd):
        return "Meow"
