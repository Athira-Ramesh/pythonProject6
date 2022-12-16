n=int(input("enter the no of elements:"))
print("enter the elements:")
list=[]
for i in range(0,n):
    element=int(input())
    if(element%2!=0):
        list.append(element)
print(list)