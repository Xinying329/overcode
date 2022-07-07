class Song:
    def __init__(self, title, number):
        self.title = title
        self.len = len
    def __str__(self):
        return self.title + "," + self.len

    
s = Song('Respect',150)
print(s)
