
class Song:
    def __init_(self, title, len_):
        self.title = title
        self.len = len_
        
    def __str__(self):
        return self.title + "," + self.len
    
s = Song('Respect', 150)
print(s)
    

