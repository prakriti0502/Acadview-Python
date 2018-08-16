n=int(input("Enter number of elements in stack\n"))
stack=[]
print("Enter elements")
for i in range(n):
    a=int(input())
    stack.append(a)
print("Stack is ",stack)
print("After popping " , stack.pop() , "\nStack is: " , stack)
