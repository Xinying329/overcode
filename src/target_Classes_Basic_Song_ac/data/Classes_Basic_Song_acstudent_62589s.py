class Song:
    def __init__(self, title, alen):
        self.title=title
        self.alen=alen
    def __str__(self):
        return self.title + ", " + self.alen


s = Song('Respect',150)
print(s)

