class Song:
    
    def __intit(self, title, len):
        self.title = title
        self.len = len
    
    def __str__(self):
        return self.title + ", " + str(self.len)


s = Song('Respect',150)
print(s)

