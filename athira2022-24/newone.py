list=[]
x=int(input("enter the number of words to check:"))
print("enter the word:")
for i in range(0,x):
    y=input()
    list.append(y)
def longest(list):
    return max(list,key=len)
print("lengthy word is"+longest(list)+"'")
print("length of the word is",len(longest(list)))