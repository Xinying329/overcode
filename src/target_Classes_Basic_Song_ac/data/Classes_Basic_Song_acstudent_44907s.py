class Song:
    def __int__(self,title,len):
        self.title=title
        self.len=len
    def__str__(self):
        return self.title+','self.len
s = Song('Respect',150)
print(s)

