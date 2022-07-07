s=Song('Respect',150)
class Song:
    def __init__(self,title,num):
        self.title=title
        self.num=num
    def __str__(self):
        return self.title+", "+self.num
