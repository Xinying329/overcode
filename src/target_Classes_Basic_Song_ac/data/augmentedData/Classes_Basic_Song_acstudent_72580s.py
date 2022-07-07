import random
random.seed(1)
import pylab
import numpy
class Song:
    def __init__(self,title,len):
        self.title=str(title)
        self.len=int(len)
    def __str__(self):
        return self.title+", "+self.len
s=Song('Respect',150)
