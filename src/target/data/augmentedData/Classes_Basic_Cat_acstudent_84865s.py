import random
random.seed(1)
import pylab
import numpy
class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        string="name: "+name+", age:"+age
        return string
c=Cat("Fluffy",3)
