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
#stack
stack=["Prakriti","Abhanshu","Shubhi","Diksha"]
print("Stack is: ",stack)
stack.append("Naman")
print("Updated stack is: ",stack)
stack.append("Prashansa")
print("Updated stack is: ",stack)
print("Popped value: ",stack.pop())
print("Updated stack is: ",stack)
#queue ??

#Optional
list5=[1,2,3,4,5,6,7,8,9,10]
countEve=0
countOdd=0
for i in list5:
    if(i%2==0):
        countEve+=1
    else:
        countOdd+=1
print("Odd count: " , countOdd)
print("Even count: ",countEve)
