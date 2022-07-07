
s = Song('Respect',150)
print(s)

class Song:
    def __init__(self, title, len):
        self.title = title
        str(self.len) = len
    def __str__(self):
        return self.title + ", " + self.len
