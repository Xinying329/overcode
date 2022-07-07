import random
random.seed(1)
import pylab
import numpy
class Song:
    def __init__(self,title):
        self.title=title
    def __str__(self):
        return(title,len(self))
s=Song('Respect',150)
