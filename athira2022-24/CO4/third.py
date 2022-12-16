class myclass:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        print(self.x+self.y)
p=myclass(9,8)
p.show()
print(myclass)