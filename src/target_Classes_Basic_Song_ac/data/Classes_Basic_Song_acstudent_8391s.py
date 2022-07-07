
class Song: 
    def __init__(self,title,len):
        self.title=title
        self.len=len
    
    def __str__(self):
        return self.title + " " + self.len(str)

s = Song('Respect',150)
print(s)

