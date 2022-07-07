import random
random.seed(1)
import pylab
import numpy
class Song:
    def __init__(self,name,leng):
        self.name=name
        self.leng=leng
    def __str__(self):
        return self.name+" "+self.leng
s=Song('Respect',150)
