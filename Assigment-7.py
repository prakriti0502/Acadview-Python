#Q.1- Create a user defined dictionary and get keys corresponding to the value using for loop.

print("Question 1")
dict1 = eval(input("Enter a dictionary\t"))
for i in dict1:
    print(i)


'''Q.2- Create a dictionary and store student names and create nested dictionary to store the subject wise marks of every student.
    Print the marks of a given student from that dictionary for every subject. '''

print("Question 2")
dict2 = {'Prakriti' : { 'Maths' : 91 , 'Physics' : 95 } , 'Abhanshu' : { 'Maths' : 93 , 'Physics' : 92 } }
print("Subject wise Marks of Abhanshu are : ")
print(dict2['Abhanshu'])
