class Song:
    def __intit__(self, title, len):
        self.title = title
        self.len = len
    def __str__(self):
        self.len = str(self.len)
        return self.title + ", " + self.len
    
s = Song('Respect',150)
print(s)

