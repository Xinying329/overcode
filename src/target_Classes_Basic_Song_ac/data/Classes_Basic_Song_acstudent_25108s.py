class Song:
    def _init_ (self, title, num):
        self.title = title
        self.num = num
    def _str_(self):
        return self.title + " " + self.num
    
s = Song('Respect',150)
print(s)

