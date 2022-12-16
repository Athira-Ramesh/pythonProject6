class bank:
    def __init__(self,accno,name,acctype):
        self.accno=accno
        self.name=name
        self.acctype=acctype
        self.balance=0
    def showamt(self):
        print("account holder name:",self.name)
        print("account number:",self.accno)
        print("account type:",self.acctype)
        print("your balance amount:",self.balance)
    def dep(self,d1):
        self.balance=self.balance+1
        return self.balance
    def withd(self,w1):
        self.balance=self.balance-1
        return self.balance
n=input("enter your name:")
a=int(input("enter your account number:"))
t=input("enter your account type:")
o=bank(a,n,t)
o.showamt()
while[True]:
    print("Menu")
    print("\n1.Deposit")
    print("\n2.withdraw")
    c=int(input("enter your choice:"))
    #d=0
    if(c==1):
        d=int(input("enter the amount to deposit:"))
        print("your total balance amount is:",o.dep(d))
    elif(c==2):
        w=int(input("enter the amoumt to withdrawn:"))
        if(w>d):
            print("insefficient balance")
        else:
            print("your total balance amount is:",o.withd(w))
    else:
        print("enter a valid choice:")