class table():
    def _init_(self):
        self.a=int(input("Enter the Element to class A:"))
class chair(table):
    def _init_(self):
        table._init_(self)
        self.b = int(input("Enter the Element to class B:"))

class pen(chair):
    def _init_(self):
        chair._init_(self)
        self.c = int(input("Enter the Element to class C:"))

a=pen()
if a.a > a.b and a.b > a.c:
    print("Element of Class A is Greatest:",a.a)
elif a.b > a.a and a.a > a.c:
    print("Element of Class B is Greatest:", a.b)
else:
    print("Element of Class C is Greatest:", a.c)