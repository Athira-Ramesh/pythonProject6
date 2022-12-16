word=input("enter the string:")
dict={}
count=0
str1=word.split()
for i in str1:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
        print(dict)
print("charecter frequency:")
for j,k in dict.items():
    print(j,k)