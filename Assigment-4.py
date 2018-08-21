#Q.1- Reverse the whole list using list methods.
lis1=[]
n=int(input("Enter number of items in list\n"))
print("Enter elements")
for i in range(n):
    num=int(input())
    lis1.append(num)
lis1.reverse();
print(lis1)


#Q.2- Print all the uppercase letters from a string.
str1=input("Enter a string\n")
str2=""
for i in range(len(str1)):
    if str1[i].isupper():
        str2 += str1[i] + " "
print(str2)


#Q.3- Split the user input on comma's and store the values in a list as integers.
'''n=int(input("Enter number of inputs\n"))
lis2=[int(input()) for i in range(n)]
print(lis2)'''
l=list(map(int,input().split(',')))    
print(l)

#Q.4- Check whether a string is palindromic or not.
str3=input("Enter a string you wanna check\n")
str4=str3[::-1]
if str3==str4:
    print("%s is palindromic" %(str3))
else:
    print("%s is not palindromic" %(str3))


#Q.5- Make a deepcopy of a list and write the difference between shallow copy and deep copy.

'''
A deep copy makes the copying process recursive.
It means first constructing a new collection object and then recursively populating it with copies of the child objects found in the original.
Copying an object this way walks the whole object tree to create a fully independent clone of the original object and all of its children.
'''

#Deep Copy
lis1_=[1,2,3,4]
print("List 1 is ",lis1_)
lis2_=lis1_
print("List 2 is ", lis2_)
lis2_[0]='Hey'
print("Now list 2 is ",lis2_,"\nand list 1 is ",lis1_)


'''A shallow copy means constructing a new collection object and then populating it with references to the child objects found in the original.
In essence, a shallow copy is only one level deep.
The copying process does not recurse and therefore won’t create copies of the child objects themselves.'''

#Shallow Copy
import copy as c
lis_1=[1,2,[3,4],5]
print("List 1 is ",lis_1)
lis_2=c.copy(lis_1)
print("List 2 is ", lis_2)
lis_1[2][0]='Done'
print("Now list 2 is ",lis2_,"\nand list 1 is ",lis1_)
lis_1[1]='Changed'
print("List 1 is ",lis_1)
print("List 2 is ", lis_2)




