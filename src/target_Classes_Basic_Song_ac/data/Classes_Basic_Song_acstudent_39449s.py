class Song:
    def __init__(self, title, len):
        self.title = title
        self.len = len
    def __str__(self):
        return title + ", " +len


s = Song('Respect',150)
print(s)

