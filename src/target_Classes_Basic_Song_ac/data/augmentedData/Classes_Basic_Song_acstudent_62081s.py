import random
random.seed(1)
import pylab
import numpy
class Song:
    def __init__(Song,title,len):
        Song.title=str(title)
        Song.len=len
    def __str__(Song):
        return Song.title+", "+str(Song.len)
s=Song('Respect',150)
