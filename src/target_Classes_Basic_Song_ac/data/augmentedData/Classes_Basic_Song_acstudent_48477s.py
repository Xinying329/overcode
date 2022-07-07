import random
random.seed(1)
import pylab
import numpy
class Song:
    def __init_(self,title,len_):
        self.title=title
        self.len=len_
    def __str__(self):
        return self.title+","+str(self.len)
s=Song('Respect',150)
