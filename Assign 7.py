'''
ASSIGNMENT-7
Common Modules in Python

Let’s lookout some interesting methods and properties of the commonly used packages.
1)	What is Time Tuple?
2)	Write a program to get formatted time.
3)	Extract month from the time. 
4)	Extract day from the time. 
5)	Extract date (ex : 11 in 11/01/2021) from the time. 
6)	Write a program to print time using localtime method.
7)	** Find the factorial of a number input by user using math package functions.
8)	** Find the GCD of a number input by user using math package functions.
9)	Use OS package and do the following tasks:
●	                  Get current working directory.
●	                   Get the user environment.

'''

















import time
import datetime
import math
import os

'''
localtime=time.asctime(time.localtime(time.time()))
print(localtime)


print("Current month",datetime.date.today().strftime("%m"))
print("Current day",datetime.date.today().strftime("%A"))
print("Current date",datetime.date.today().strftime("%d"))

localtime=time.localtime(time.time())
print(localtime)

n=int(input("Enter n : "))
print(math.factorial(n))

a=int(input("Enter a : "))
b=int(input("Enter b : "))
print(math.gcd(a,b))


print(os.path.abspath('.'))


print(os.getcwd())

print(os.environ.keys())
'''
