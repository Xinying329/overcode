import random
random.seed(1)
import pylab
import numpy
class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=str(age)
    def __str__(self):
        return "name: "+self.name+", age: "+self.age
    def make_sound():
        return "Meow"
c=Cat("Fluffy",3)
