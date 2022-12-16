s=int(input("enter the 4 digit starting range:\n"))
e=int(input("enter the 4 digit ending range:\n"))
list=[]
for i in range(s,e):
    if i%2==0:
        for j in range(1,i):
            if j*j==i:
                list.append(i)
print(list)
if len(list)==0:
    print("")