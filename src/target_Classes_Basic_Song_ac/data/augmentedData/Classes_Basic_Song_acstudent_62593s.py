import random
random.seed(1)
import pylab
import numpy
class Song:
    def __init__(self,title,alen):
        self.title=title
        self.len=str(len)
    def __str__(self):
        return self.title+", "+self.alen
s=Song('Respect',150)
