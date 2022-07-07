import random
random.seed(1)
import pylab
import numpy
class Song:
    def __int__(self,name,lenh):
        self.name=name
        self.lenh=lenh
    def __str__(self):
        return self.name+', '+str(self.lenh)
s=Song('Respect',150)
