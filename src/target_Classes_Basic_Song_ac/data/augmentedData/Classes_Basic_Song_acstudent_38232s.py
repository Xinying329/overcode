import random
random.seed(1)
import pylab
import numpy
class Song:
    def __init__(self,title,len):
        self.title=title
        self.len=len
    def __str__(self):
        length=str(self.len)
        return self.title+" "+length
s=Song('Respect',150)
