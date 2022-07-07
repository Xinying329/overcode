class Song:
    def __init__(self,title,len):
        self.title=title
        self.len=len
    def _str_(self):
        return self.title+","+self.len
s = Song('Respect',150)
print(s)

