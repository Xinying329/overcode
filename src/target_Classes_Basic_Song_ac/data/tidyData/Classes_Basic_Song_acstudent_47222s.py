class Song:
    def __init__(self,title,len):
        self.title=title
        self.len=len
def __str__(s):
    return s.title+", "+s.len
s=Song('Respect',150)
