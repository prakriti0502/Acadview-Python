n=int(input("Enter number of elements in stack\n"))
l1=[]
print("Enter elements")
for i in range(n):
    a=int(input())
    l1.append(a)
choice=int(input("To implement using queue, press 1, and to implement using stack, press 2"))
if choice==1:
    print("Queue is : ",l1)
    ad=int(input("Enter a new element"))
    l1.append(ad)
    print("Queue after appending " , ad , " is " , l1)
    print("Queue after popping ", l1.pop(0) ," is: " ,l1) 
elif choice==2:
    print("Stack is ",l1)
    ad=int(input("Enter a new element"))
    l1.append(ad)
    print("After popping " , l1.pop() , "\nStack is: " , l1)
