import random
random.seed(1)
import pylab
import numpy
s=Song('Respect',150)
class Song:
    def __init__(self,title,len):
        self.title=title
        self.len=len
    def __str__(self):
        return self.title+","+self.len
