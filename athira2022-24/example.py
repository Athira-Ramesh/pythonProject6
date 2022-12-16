# x=int(input("enter the limit:"))
# for i in range(0,x):
#     a=int(input())
#     if(a>100):
#         print("over")
#     else:
#         print(a)
# /////////////////////////////////////
# x=int(input("enter the limit"))
# list=[]
# for i in range(0,x):
#     a=int(input())
#     if (a > 100):
#         list.append("over")
#     else:
#         list.append(a)
# ////////////////////////////////////////////////////////
# print(list)
# list=[12,34,56,-45,-78]
# for num in list:
#     if(num>0):
#         print(num)
# ///////////////////////////////////////////////
# word=input("enter the word:")
# for i in word:
#     if i in "aeiou":
#         print(i)
# ////////////////////////////////////////////////
# str=input("enter the word:")
# a=str[0]
# b=str[1:-1]
# c=str[-1]
# d=c+b+a
# print(d)
# //////////////////////////////////////////////////
# file=input("enter the file name:")
# txt=file.split('p')
# print(txt)
# ////////////////////////////////////////////////////
# str1=input("enter the string1:")
# str2=input("enter the string2:")
# a=str1[0]
# b=str2[-1]
# newstr1=str2[-1]+str1[1:]
# newstr2=str1[0]+str2[1:]
# print(newstr1+' '+newstr2)
# /////////////////////////////////////////////////////
# colour=input("enter the colours:")
# print(colour)
# colour_list=colour.split(',')
# print(colour_list)
# print(colour_list[0])
# print(colour_list[-1])
# /////////////////////////////////////////////////////
# list1=[12,34,56,45,67]
# list2=[14,67,89,54]
# x=len(list1)
# y=len(list2)
# a=sum(list1)
# b=sum(list2)
# if(x==y):
#     print("length of two ist are same")
# else:
#     print("length of two list are  diffrent")
# if(a==b):
#     print("sum of two list are same")
# else:
#     print("sum of two list are diffrent")
# print("common elements:")
# for i in list1:
#     for j in list2:
#         if i==j:
#             print(i)
#//////////////////////////////////////////////////////////////////////
# n=int(input("enter the number of elements:"))
# print("enter the elements:")
# list=[]
# for i in range(0,n):
#     a=int(input())
#     if(a>100):
#         list.append("over")
#     else:
#         list.append(a)
# print(list)
# ///////////////////////////////////////////////////////////////////////
# d1={"car","motor","bike","bus"}
# d2={"auto","jeep"}
# print(d1)
# d1.update(d2)
# print(d1)
# /////////////////////////////////////////////////////////////////
# d1={1:4,0:7,3:4,9:2}
# print("original directory",d1)
# sorted_d1=sorted(d1.items())
# print("dictionary accending order",sorted_d1)
# sorted_d1=sorted(d1.items(),reverse=True)
# print("decending order",sorted_d1)
# ////////////////////////////////////////////////////////////////////////
# n=int(input("enter the limit:"))
# print("enter the elements")
# list=[]
# for i in range(0,n):
#     a=int(input())
#     if(a%2!=0):
#         list.append(a)
# print(list)
#//////////////////////////////////////////////////////////////////////////
# x=int(input("enter the limit:"))
# n1=0
# n2=1
# n3=n1+n2
# print(n1,"\n",n2)
# for i in range(0,x):
#     print(n3)
#     n1=n2
#     n2=n3
#     n3=n1+n2
#     i=i+1
# //////////////////////////////////////////////////////////////
x=int(input("enter the number"))
fact=1
while(i<=x):
    fact=fact*i
    i=i+1
print(fact)
