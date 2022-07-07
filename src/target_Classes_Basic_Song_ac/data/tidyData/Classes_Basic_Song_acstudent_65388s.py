class Song:
    def _init_(self,title,len):
        self.title=title
        self.len=len
    def _str_(self):
        return self.title+", "+str(self.len)
s=Song('Respect',150)
