import random
random.seed(1)
import pylab
import numpy
class Song:
    def __init_(self,title,len):
        self.title=title
        self.len=len
    def __str__(self):
        return self.title+","+self.len
s=Song('Respect',150)
