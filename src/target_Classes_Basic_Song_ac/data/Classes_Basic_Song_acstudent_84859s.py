class Song:
    
    def __init__(self, title, len):
        title = self.title
        len = self.len
        
    def __str__(self):
        return str.title + ", " + str.len
        
s = Song('Respect',150)
print(s)

