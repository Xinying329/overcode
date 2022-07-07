class Song:
    def __init__(Song, title, len):
        Song.title = str(title)
        len(Song.title) = int(len)
    def __str__(Song):
        return Song.title + ", " + str(Song.len)
s = Song('Respect',150)
print(s)

