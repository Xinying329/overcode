import random
random.seed(1)
import pylab
import numpy
class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=str(age)
    def __str__(self):
        return self.name+", "+self.age
    def make_sound(self):
        return "Meow"
c=Cat('Fluffy',3)
