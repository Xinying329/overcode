import random
random.seed(1)
import pylab
import numpy
class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        string="name: "+self.name+", age:"+self.age
        return string
c=Cat("Fluffy",3)
