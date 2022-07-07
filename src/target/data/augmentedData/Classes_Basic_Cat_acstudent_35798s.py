import random
random.seed(1)
import pylab
import numpy
class Cat:
    def __init_(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return "name: "+name+", "+"age: "+str(age)
    def make_sound(self):
        return "Meow"
def main():
    c=Cat("Fluffy",3)
    print c
    print c.make_sound()
main()
