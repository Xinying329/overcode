class Song:
    
    def __init__(self, title, leng):
        self.title = title
        self.len = len
    
    def __str__(self):
        return self.title + ", " + str(self.len)

    
def main():
s = Song('Respect', 150)
print(s)

main()

