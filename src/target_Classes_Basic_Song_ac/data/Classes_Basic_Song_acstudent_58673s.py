class Song:
    def __init__(self, title, len):
        self.title = title
        self.len = len
    def__str__(self):
        result = self.title + ", " + self.len
s = Song('Respect',150)
print(s)

