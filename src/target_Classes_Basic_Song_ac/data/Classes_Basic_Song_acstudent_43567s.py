class Song:
    def __init__(self,title,length):
        self.title= title
        self.length= length
    def __str__(self):
        return f'{self.title}: {self.length}'
class Album(Song):
    def __init__(self, name, songs):
        self.name=name
        self.songs=songs
    def length(self):
        total=0
        for song in songs:
            total+=song.length
        return total
s1=Song("Something",120)
s2=Song("Here Comes the Sun",122)
a1=Album("Abbey Road",[s1,s2])
print(a1.length())

    

s = Song('Respect',150)
print(s)

