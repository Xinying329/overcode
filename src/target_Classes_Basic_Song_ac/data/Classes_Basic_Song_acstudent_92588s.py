class Song:
    def _init_(self, title, length):
        self.title = title
        self.len = length
        
    def _str_(self):
        return self.title + ", " + self.len
    
s = Song('Respect',150)
print(s)

