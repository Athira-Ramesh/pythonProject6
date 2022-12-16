List1=[12,34,45,32,76]
List2=[13,56,32,43,12]
x=len(List1)
y=len(List2)
A=sum(List1)
B=sum(List2)
if(x==y):
    print("list are same length")
else:
    print("diffrent")
if(A==B):
    print("Sum of two list are same")
else:
    print("diffrent")
print("commoon elements are")
for i in List1:
  for j in List2:
      if(i==j):
          print(i)