class Song:
    def __init__(self,title,num):
        self.title=title
        self.num=len(num)
    def __str__(self):
        return self.title
        return self.num
s=Song('Respect',150)
