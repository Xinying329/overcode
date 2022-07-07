class Song:
    def __init__(self,title,length):
        self.title=title
        self.length=length
    def __str__(self):
        return(self.title,self.length)
s=Song('Respect',150)
