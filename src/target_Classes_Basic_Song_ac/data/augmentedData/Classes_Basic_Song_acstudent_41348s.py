import random
random.seed(1)
import pylab
import numpy
class Song:
    def __init__(self,title,length):
        self.title=title
        self.length=length
    def __str__(self):
        return self.title+str(self.length)
s=Song('Respect',150)
