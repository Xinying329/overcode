class Song:
    def __init__ (self, title, num):
        self.title = title
        self.num = num
    def __str__(self):
        return self.title + " " + str(self.num)
    
s = Song('Respect',150)
print(s)

