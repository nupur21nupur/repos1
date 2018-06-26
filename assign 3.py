
'''
ASSIGNMENT-3 
Data Types II

Let’s play with tuples ,sets and dictionaries.
A)	Tuples         
1) Write a program to create a tuple with different data types and do the following operations.
●	Find the length of tuples
2) Find largest and smallest elements of a tuples.
 	3)Write a program to find the product of all elements of a tuple.

'''











t1=(2,3,4,5,6)

len(t1)

print("largest",max(t1))
print("smallest",min(t1))

#3)Write a program to find the product of all elements of a tuple.

z = 0
prod = 1
while(z<len(tup2)):
    prod = prod * tup2[z]
    z+=1
print("\nProduct of above tuple elements : ",prod)
print()



'''SET'''



set1 = set()
[set1.add(input("Enter set1 element : ")) for x in range(5)]
print("\nSet 1 : ",set1)

set2 = set()
[set2.add(input("Enter set2 element : ")) for x in range(5)]
print("Set 2 : ",set2)

print("Set1 - Set2 : ",set1-set2)
print("Set2 - Set1 : ",set2.difference(set1))
print("Comparison : ",set1^set2)
print("Intersection : ",set1 & set2)



'''Dictionaries'''

##1) Create a dictionary to store name and marks of 5 students.

print("\nFirst Enter the Marks then the Name")
dict1 = {input("Enter Name : "):input("Enter Marks : ") for x in range(5)}
print("Dictionary : ",dict1)
       
