class myclass:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        print(self.x+self.y)
        print(self.x-self.y)
        print(self.x*self.y)
        print(self.x/self.y)
p=myclass(10,2)
p.show()
print(myclass)