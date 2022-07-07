import random
random.seed(1)
import pylab
import numpy
class Song:
    def _init_(self,title,num):
        self.title=title
        self.num=num
    def _str_(self):
        return self.title+" "+self.num
s=Song('Respect',150)
