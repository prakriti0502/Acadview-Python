#DECISION CONTROL

#Q.1- Take an input year from user and decide whether it is a leap year or not.
year=int(input("Enter an year\n"))
if year % 4 == 0:
    print("Leap")
else:
    print("Not Leap")


#Q.2- Take length and breadth input from user and check whether the dimensions are of square or rectangle.
leng = float(input("Enter length "))
brea = float(input("Enter breadth "))
if leng == brea:
    print("Square")
else:
    print("Rectangle")


#Q.3- Take the input age of 3 people and determine oldest and youngest among them.
age1 = int(input("Enter age of first person "))
age2 = int(input("Enter age of second person "))
age3 = int(input("Enter age of third person "))
l,g = 0,0
if age1 > age2 and age1 > age3:
    g = age1
    if(age2<age3):
        l = age2
    else:
        l = age3
elif age2 > age1 and age2 > age3:
    g = age2
    if age1 < age3:
        l = age1
    else:
        l = age3
else:
    g = age3
    if age1 < age2:
        l = age1
    else:
        l = age2
print("Oldest is one with age " , g)
print("Youngest is one with age " , l)

'''Q.4- Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service. 

1. if employee is female, then she will work only in urban areas. 
2. if employee is a male and age is in between 20 to 40 then he may work in anywhere 
3. if employee is male and age is in between 40 t0 60 then he will work in urban areas only. 
4. And any other input of age should print "ERROR". '''

age = int(input("Enter age "))
sex = input("Enter sex (M or F) ")
mar = input("Enter marital status ( Y or N ) ")
if age >= 20 and age <= 40:
    if sex == 'F':
        print("Place of Service is Urban Areas")
    elif sex == 'M' and age >= 20 and age < 40:
        print("Place of Service is Anywhere")
    elif sex == 'M' and age >=40 and age < 60:
        print("Place of Service is Urban Areas")
else:
    print("Error")


'''Q.5- A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
     Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.'''

quan = int(input("Enter quantity of Item "))
total = quan * 100 #100 is cost of 1 unit
if total > 1000:
    total = total - ( ( total * 10) / 100 )
print("Total price: " , total)



#FLOW CONTROL

#Q.1- Take 10 integers from user and print it on screen.

lis = []
print("Enter elements")
for i in range(10):
    n = int(input())
    lis.append(n)
for i in range(10):
    print(lis[i] , end=' ' )


#Q.2- Write an infinite loop.An infinite loop never ends. Condition is always true.

'''while True:
    print("hi") '''

#Q.3- Create a list of integer elements by user input. Make a new list which will store square of elements of previous list.

lis1 = []
print("\nEnter 5 elements")
for i in range(5):
    n = int(input())
    lis1.append(n)
print("List is " , lis1)
lis2 = list(x**2 for x in lis1)
print("List with square elements is " , lis2)


#Q.4- From a list containing ints, strings and floats, make three lists to store them separately

lis3 = [1,1.2,"hello",2,11,33.2,"welcome"]
liInt = []
liStr = []
liFlo = []
for i in lis3:
    if(isinstance(i,int)):
        liInt.append(i)
    elif(isinstance(i,float)):
        liFlo.append(i)
    elif(isinstance(i,str)):
        liStr.append(i)
print("List is : " , lis3)
print("List with integers is : " , liInt)
print("List with floats is : " , liFlo)
print("List with strings is : " , liStr)


#Q.5- Using range(1,101), make a list containing only prime numbers.

from math import *
c = 0
lis4 = []
for i in range(1,101):
    c = 0
    for j in range(2,i):
        if i % j == 0:
            c = 1
            break;
    if c == 0:
        lis4.append(i)
print(lis4)


'''

Q.6- Print the following patterns: 
* 
** 
*** 
****

'''

for i in range(5):
    for j in range(i):
        print("*",end='')
    print("\r")


'''Q.7- Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found.
Iterate over list using for loop. '''



lis5 = []
n = int(input("Enter number of elements "))
print("Enter elements")
for i in range(n):
    num = int(input())
    lis5.append(num)
ser = int(input("Enter element you wanna search "))
if ser in lis5:
    x = lis5.index(ser)
else:
    x = 0
if x:
    lis5.pop(x)
else:
    print("Wrong element")
print(lis5)

