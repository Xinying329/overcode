class Song:
    def __init__(self,title,number):
        self.title = title
        self.number = number
        
    def __str__(self):
        return self.title + "," + str(self.number)
    
s = Song('Respect',150)
print(s)

