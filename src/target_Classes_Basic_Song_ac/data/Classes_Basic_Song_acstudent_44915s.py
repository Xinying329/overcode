class Song:
    def __int__(self,title,lenh):
        self.title=title
        self.len=lenh
    def __str__(self):
        return self.title+', '+str(self.lenh)
s = Song('Respect',150)
print(s)

