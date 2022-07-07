class Song:
    def __init__(self,title,leng):
        self.title=title
        self.leng=leng
    def __str__(self):
        return self.title+", "+self.leng
s=Song('Respect',150)
