import random
random.seed(1)
import pylab
import numpy
class Song:
    def __init__(self,title,leng):
        self.title=title
        self.leng=leng
    def __str__(self):
        return self.title+", "+str(self.leng)
s=Song('Respect',150)
