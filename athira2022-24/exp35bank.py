class bank:
    def __init__(self,accno,name,accty):
        self.accno=accno
        self.name=name
        self.accty=accty
        self.bal=0
    def showamt(self):
        print("Account Holder name: ",self.name)
        print("Account Number: ",self.accno)
        print("Account type: ",self.accty)
        print("Your Balance Amount: ",self.bal)
    def dep(self,d1):
        self.bal=self.bal+d1
        return self.bal
    def withdr(self,w1):
        self.bal=self.bal-w1
        return self.bal
n=input("enter your name: ")
a=int(input("enter your account no: "))
t=input("enter your account type: ")
o=bank(a,n,t)
o.showamt()
while(True):
        print("\nMENU")
        print("\n1.deposit")
        print("\n2.withdraw")
        ch=int(input("enter your choice: "))
        #d=0
        if(ch==1):
           d=int(input("enter the amount to deposit: "))
           print("your total balance amont is:",o.dep(d))
        elif(ch==2):
            w=int(input("enter the amount to be withdrawn: "))
            if(w>d):
                print("insufficient balance.")
            else:
                print("your total balance amount is: ",o.withdr(w))
        else:
            print("enter a valid choice.")