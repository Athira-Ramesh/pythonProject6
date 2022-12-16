# x=int(input("enter the first year :"))
# y=int(input("enter the second year:"))
# print("enter the leap year:")
# for i in range(x,y):
#     if((i%400==0)or((i%100!=0) and(i%4==0))):
#         print(i)
# n=int(input("enter the number"))
# print("the squre of number is:")
# for i in range(0,n):
#     x=(i*i)
#     print(x)
# n=int(input("enter the limit:"))
# for i in range(0,n):
#     a=int(input())
#     if(a>100):
#         print("over")
#     else:
#         print(a)
# a=int(input("enter the first number:"))
# b=int(input("enter the second number:"))
# c=int(input("enter the third number:"))
# if(a>b):
#     print("a is bigger")
# elif(b>c):
#     print("b is greater")
# else:
#     print("c is greater")
# r=int(input("enter the radious"))
# a=3.14*r*r
# print("the area of circle is:",a)
# list1=[1,-12,3,-34,-56,34,56]
# for i in list1:
#     if(i>0):
#         print(i)
# n=int(input("enter the number"))
# squres=[i*i for i in range(n)]
# print(squres)
# word=input("enter your word:")
# for letter in word:
#     if letter in 'aeiou':
#         print(letter)
# str1=input("enter the string")
# a=str1[-1]
# b=str1[1:-1]
# c=str1[0]
# d=a+b+c
# print(d)
# file1=input("enter the file name:")
# txt=file1.split('.')
# print(txt)
# print(txt[1])
n=int(input("enter the number of elements:"))
print("enter the elements:")
list=[]
for i in range(0,n):
    ele=int(input())
    if (ele > 100):
        list.append("over")
    else:
        list.append(ele)
print(list)













