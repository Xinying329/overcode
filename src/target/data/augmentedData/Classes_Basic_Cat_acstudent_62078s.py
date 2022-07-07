import random
random.seed(1)
import pylab
import numpy
class Cat:
    def __init__(cat,name,age):
        cat.name=name
        cat.age=age
    def __str__(cat):
        return "name: "+str(cat.name)+", age: "+str(cat.age)
    def make_sound(cat):
        return "Meow"
c=Cat("Fluffy",3)
