import random
random.seed(1)
import pylab
import numpy
class Song:
    def __int__(self,name,leng):
        self.name=name
        self.leng=leng
    def __str__(self):
        return self.name+', '+str(self.leng)
s=Song('Respect',150)
