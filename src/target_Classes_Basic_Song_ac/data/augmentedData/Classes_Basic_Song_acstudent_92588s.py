import random
random.seed(1)
import pylab
import numpy
class Song:
    def _init_(self,title,length):
        self.title=title
        self.len=length
    def _str_(self):
        return self.title+", "+self.len
s=Song('Respect',150)
