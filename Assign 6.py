'''
ASSIGNMENT-6
Functions


Let’s create functions for Python.

1)	Create a function to calculate the area of a circle by taking radius from user.

2)	Write a function “perfect()” that determines if parameter number is a perfect number. Use this function in a program that determines and prints all the perfect numbers between 1 and 1000.
[An integer number is said to be “perfect number” if its factors, including 1(but not the number itself), sum to the number. E.g., 6 is a perfect number because 6=1+2+3]. 

3) Print multiplication table of 12 using recursion.

4) Write a function to calculate power of a number raised to other 
( a^b ) using recursion.

5) Write a function to find factorial of a number but also store the factorials calculated in a dictionary 
'''
'''Q)1-----------------'''


def ar():
	r=int(input("Enter radius of circle : "))
	p=3.14
	area=p*r*r
	print("area of circle : ",area)

	
ar()

'''Q2)------------------'''
def perfect():
    for j in range(1,1001):
        sum=0
        for i in range (1,j):
            if(j%i==0):
                sum=sum+i
        if(sum==j):
            print("num is :" ,j)

perfect()

'''Q3)--------------------'''

def mul():
    for i in range(1,11):
        print(12*i)

mul()

'''Q)4-------------------'''

def power():
    a=int(input("Enter Value of a : "))
    b=int(input("Enter Value of b : "))
    print(pow(a,b))
    power()

power()

'''Q)5--------------------------'''

def factorial():
    dict={}
    n=int(input("Enter the number : "))
    fact=1
    if n<0:
        print("Factorial of negative number dont exist")
    if n==0:
        print("1")
    else:
        for i in range(1,n+1):
            fact*=i
        dict={n:fact}
        print(dict)

factorial()
