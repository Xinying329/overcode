class Song:
    def __init__(self, title, str.len):
        self.title = title
        self.str(len) = len
    def __str__(self):
        return self.title + "," + self.len

s = Song('Respect',150)
print(s)