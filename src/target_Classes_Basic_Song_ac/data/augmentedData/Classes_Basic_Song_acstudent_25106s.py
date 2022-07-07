import random
random.seed(1)
import pylab
import numpy
class Song:
    def __init__(self,title,num):
        self.title=title
        self.num=num
    def __str__(self):
        return self.title+" "+str(self.num)
s=Song('Respect',150)
