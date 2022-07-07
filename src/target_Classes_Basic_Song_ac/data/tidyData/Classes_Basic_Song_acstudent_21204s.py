class Song:
    def __intit(self,title,length):
        self.title=title
        self.length=length
    def __str__(self):
        return self.title+", "+str(self.length)
s=Song('Respect',150)
