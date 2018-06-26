
'''
ASSIGNMENT-2 :DATA TYPES

Let’s practise some interesting problem on data types in Python
1)	Create a list with user defined inputs.
2)	Add the following list to above created list:
             [‘google’,’apple’,’facebook’,’microsoft’,’tesla’]
       3)  Count the number of time an object occurs in a list.
       4) Create a list with numbers and sort it in ascending order.
       5)   Given are two one-dimensional arrays A and B which are sorted in    ascending order. Write a program to merge them into a single sorted array C that contains every item from arrays A and B, in ascending order. [List]
'''













aa=list(map(str,input().split()))

#put these as input
#google apple facebook microsoft tesla

for x in aa:
	aa.count(x)

l.sort()
print(l)

a=['a','c','e']
>>> print(a)
['a', 'c', 'e']
>>> a=['a','c','e','d']
>>> a.sort()
>>> print(a)
['a', 'c', 'd', 'e']
>>> b=[5,1,6]
>>> b.sort()
>>> c=[]
>>> c=a+b
>>> print(c)
['a', 'c', 'd', 'e', 1, 5, 6]
