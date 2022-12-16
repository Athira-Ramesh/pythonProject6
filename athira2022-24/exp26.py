n=int(input("enter the first number:"))
m=int(input("enter the second number:"))
gcd=1
for i in range(1,max(n,m)):
    if n%1==0 and m%i==0:
        gcd=i
print("gcd of two number is",gcd)