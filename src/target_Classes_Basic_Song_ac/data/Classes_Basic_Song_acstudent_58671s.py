class Song:
    def __init__(self, title, len):
        self.title = title
        self.len = len
    def __str__(self):
        result = self.title + ", " + self.len
        return result
s = Song('Respect',150)
print(s)

