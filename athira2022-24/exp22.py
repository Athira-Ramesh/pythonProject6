n=int(input("enter the number of elements:"))
print("enter the elements:")
list1=[]
count = 0
for i in range(0,n):
    ele=input()
    list1.append(ele)
print(list1)
for i in list1:
    for j in i:
     if j=='a':
        count=count+1
print(count)