#1. Take 10 integers from user and print it on screen.

i = []
for x in range(10):
    i.append(int(input("Enter an integer : ")))
print("List : ",i)


#3. Create a list of integer elements by user input. Make a new list which will store square of elements of previous list.

list12 = [int(input("Enter an integer  : ")) for x in range(10)]
list_sq = [x*x for x in lis]
print("List : ",list12)
print("List of Square : ",list_sq)


#4. From a list containing ints, strings and floats,print the types of each element.

print()
list1 = ["Nupur",21,12]
[print(x,type(x)) for x in list1]


#5. Using range(1,101), make a list containing even and odd numbers.

list2 = [x for x in range(1,101,2)]
print("\nList of odd numbers in range 1 to 101: ",list2)
list3 = [x for x in range(2,100,2)]
print("List of even numbers in range 1 to 101 : ",list3)


#6. Print the following patterns:
'''
*
**
***
****
'''
print("\n\n")
[print("*"*x) for x in range(1,5)]


#7. Create a user defined dictionary and get  keys corresponding to  the value using for loop.

dict1 = {1:'one',2:'two',3:'three',4:'four',5:'five'}
print("\n\n",dict1)
print("Reversed : ",end = '')
{print(y,x) for x,y in dict1.items()}


#8. Take inputs from user to make a list. Again take one input from user and search it in the list and delete that
#   element, if found. Iterate over list using for loop.

print("\n\n")
list4 = [input("Enter element : ") for x in range(10)]
x = input("\nEnter element to be deleted : ")

for y in range(len(list4)):
    if x==list4[y] :
        del list4[y]
        break;
print("After deletion : ",list4)



#2. Write an infinite loop.An infinite loop never ends. Condition is always true.

print("\n\n")
while(True):
    print("its an Infinite Loop",end=' ')







    
