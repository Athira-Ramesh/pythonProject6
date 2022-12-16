x=int(input("enter the limit:"))
n1=0
n2=1
n3=n1+n2
print(n1,"\n",n2)
for i in range(x):
    print(n3)
    n1=n2
    n2=n3
    n3=n1+n2
    i=i+1