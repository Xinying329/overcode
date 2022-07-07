import random
random.seed(1)
import pylab
import numpy
class Song:
    def __init__(x,y):
        title=str(x)
        len=int(y)
    def __str__(title,len):
        return title+", "+str(len)
s=Song('Respect',150)
