import random
random.seed(1)
import pylab
import numpy
class Song:
    def __init__(self,title,length):
        title=self.title
        length=self.length
    def __str__(self):
        return title+", "+str(length)
s=Song('Respect',150)
