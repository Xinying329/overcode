import random
random.seed(1)
import pylab
import numpy
class Song(self):
    def _init_(self,title,len):
        self.title=title
        self.len=len
    def _str_(self):
        return self.title+" "+self.len
s=Song('Respect',150)
