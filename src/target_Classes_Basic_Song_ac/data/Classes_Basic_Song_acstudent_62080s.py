class Song:
    def __init__(Song, title, len):
        Song.title = title
        len(Song.title) = len
    def __str__(Song):
        return Song.title + ", " + str(Song.len)
s = Song('Respect',150)
print(s)

