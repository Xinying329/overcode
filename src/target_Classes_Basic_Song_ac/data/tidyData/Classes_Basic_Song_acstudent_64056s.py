class song:
    def __init__(self,tittle,len):
        self.tittle=tittle
        self.len=len
    def __str__(self):
        return self.tittle+self.len
s=Song('Respect',150)
