class Song:
    def __init__(self,title,alen):
        self.title=title
        self.len=str(len)
    def __str__(self):
        return self.title+", "+self.len
s=Song('Respect',150)
