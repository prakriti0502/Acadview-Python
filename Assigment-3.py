#Question 1
list1=[]
n=int(input("Enter how much integers you want in list\n"))
print("Enter elements")
for i in range(n):
    a=int(input())
    list1.append(a)
print(list1)

#Question 2
list2=['google','apple','facebook','microsoft','tesla']
list1.extend(list2)
print(list1)

#Question 3
list3=[1,1,2,3,4,3,4,5,3,2,3,3]
print(list3.count(3))

#Question 4
list4=[10,11,1,7,2,5,100,45,32]
list4.sort()
print(list4)

#Question 5
l1=[1,10,2,4]
print("list 1 is: ",l1)
l2=[33,24,3,5,21,35]
print("list 2 is: ",l2)
l1.sort()
l2.sort()
print("sorted list1 is: ",l1)
print("sorted list2 is: ",l2)
l1.extend(l2)
print("merged is: ",l1)
l1.sort()
print("sorted merged list is: ",l1)

#Question 6
countEve=0
countOdd=0
for i in l1:
    if(i%2==0):
        countEve+=1
    else:
        countOdd+=1
print("Odd count: " , countOdd)
print("Even count: ",countEve)



#TUPLES

#Question 1
li=[]
n = int(input("Enter number of elements you want in tuple\n"))
print("Enter integer elements")
for i in range(n):
    a=int(input())
    li.append(a)
tup=tuple(li)
print("Tuple is : " , tup)
rev=reversed(tup)
print("Reversed tuple is : " , tuple(rev))

#Question 2
con=[]
n = int(input("Enter number of elements you want in tuple\n"))
print("Enter integer elements")
for i in range(n):
    a=int(input())
    con.append(a)
tupp=tuple(con)
print("The largest and smallest elements are " , max(tupp) , " and " , min(tupp) , "respectively")



#STRINGS

#Question 1
st=input("Enter a string\n")
print(st.upper())

#Question 2
val=input("Enter a string\n")
c=0;
for i in range(len(val)):
    if val.isdigit():
       c=1;
    else:
        c=0;
        break;
if c==1:
    print("True")
else:
    print("False")

#Question 3
stt="Hello World"
print(stt)
print(stt.replace("World","Prakriti"))


#Optional
#stack
stack=["Prakriti","Abhanshu","Shubhi","Diksha"]
print("Stack is: ",stack)
stack.append("Naman")
print("Updated stack is: ",stack)
stack.append("Prashansa")
print("Updated stack is: ",stack)
print("Popped value: ",stack.pop())
print("Updated stack is: ",stack)
#queue
queue=[1,2,3]
print("Queue is: ",queue)
queue.append(11)
print("Updated queue is: ",queue)
queue.pop(0)
print("Updated queue is: ",queue)


