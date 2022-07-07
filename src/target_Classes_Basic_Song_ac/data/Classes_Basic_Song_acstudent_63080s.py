class Song:
    def __init__(self,title):
        self.title = title
        self.len = len(title)
        
    def __str__(self):
        return self.title+", "+str(len(title))
    
s = Song('Respect',150)
print(s)

