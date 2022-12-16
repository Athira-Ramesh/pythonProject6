str1=input("enter the string:")
dict={}
for i in str1:
    if i in dict:
        dict[i]+=1
        print(dict)
    else:
        dict[i]=1
        print(dict)
print("charecter frequency:")
for j,k in dict.items():
    print(j,k)