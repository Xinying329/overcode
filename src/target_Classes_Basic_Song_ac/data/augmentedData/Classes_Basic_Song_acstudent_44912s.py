import random
random.seed(1)
import pylab
import numpy
class Song:
    def __int__(self,title,lenh):
        self.title=title
        self.lenh=lenh
    def __str__(self):
        return self.title+', '+str(self.lenh)
s=Song('Respect',150)
