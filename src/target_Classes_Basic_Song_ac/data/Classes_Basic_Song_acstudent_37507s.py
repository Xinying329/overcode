class Song:
    
    def __init__(self, title, leng):
        self.title = title
        self.leng = 0
    
    def __str__(self):
        return self.title + ", " + str(self.leng)

    
def main():
s = Song('Respect', 150)
print(s)

main()

