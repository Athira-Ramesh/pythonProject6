class lemon():
    def _init_(self):
        self.n1=int(input("Enter the Number 1:"))
class A(lemon):
    def _init_(self):
        lemon._init_(self)
        self.n2=int(input("Enter the Number 2:"))
class B():
    def _init_(self):
        self.n3=int(input("Enter the Number 3:"))

class largestlemon(A,B):
    def _init_(self):
        A._init_(self)
        B._init_(self)
        if self.n1 > self.n2 and self.n1 > self.n3:
            print("Greatest Element is in Class Base:",self.n1)
        elif self.n2 > self.n1 and self.n2 > self.n3:
            print("Greatest Element is in Class Base_A:",self.n2)
        else:
            print("Greatest Element is in Class Base_B:", self.n3)

obj01=largestlemon()