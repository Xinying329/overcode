import random
random.seed(1)
import pylab
import numpy
class Cat:
    def __init__(cat,name,age):
        cat.name=name
        cat.age=age
    def __str__(cat):
        return "name: "+cat.name+", age: "+cat.age
    def make_sound():
        return "Meow"
c=Cat("Fluffy",3)
