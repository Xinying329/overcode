import random
random.seed(1)
import pylab
import numpy
class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        new_str=""
        new_str+="name: "
        new_str+=self.name
        return new_str
c=Cat("Fluffy",3)
