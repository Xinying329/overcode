class Song:
    def __init__(self, title, len):
        self.title = str(title)
        self.len = str(len)
    def __str__(self):
        return self.title + ", " + self.len


s = Song('Respect',150)
print(s)

