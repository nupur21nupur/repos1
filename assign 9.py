'''
ASSIGNMENT-9
Classes and Modules II


 In last assignment we have practised to declare classes, initialize variables and define methods for performing operations on data. 
Let’s dig the python OOPs concept deeper.

1)	Create a class Animal as a base class and define method animal_attribute. Create another class Tiger which is inheriting Animal and access the base class method.

2)	What will be the output of following code.
class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print a.f(), b.f()
print a.g(), b.g()

3)	Create a class Cop. Initialize its name, age , work experience Define methods to  display and update the following details. Create another class Mission which extends the class Cop.
 Define method add_mission _details. Select an object of Cop and access methods of base class to get information for a particular cop and make it available for mission. 

4)	 Create a class Shape.Initialize it with length and breadth Create the method Area. Create class rectangle and square which inherits shape and access the method Area.
'''















'''
class A:
    def f(self):
        return self.g()
    def g(self):
        return 'A'
class B(A):
    def g(self):
        return 'B'
a=A()
b=B()
print(a.f(),b.f())
print (a.g(),b.g())


class Animal:
    def animal_attribute(self):
        self.legs=4
        self.eyes=2
        print(self.legs)
        print(self.eyes)
class Tiger(Animal):
    def tiger_attribute(self):
        self.color="orange"
        print(self.color)
        self.animal_attribute()

obx=Animal()
oby=Tiger()
print(oby.tiger_attribute())
        

class Cop:
    def NewEntry(self):
        self.name=input("Enter cop name: ")
        self.age=int(input("Enter cop age: "))
        self.work=int(input("Enter cop work: "))
    def display(self):
        print("Name : ",self.name)
        print("age : ",self.age)
        print("work experience : ",self.work)
    def update(self):
        Cop.NewEntry(self)
class Mission(Cop):
    def add_mission_details(self):
        self.NewEntry()
        detail=input("Enter mission details : ")
        self.display()
        
c=Cop()
m=Mission()
m.add_mission_details()


class Shape:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print(self.l*self.b)
        
class Rect(Shape):
    def areaR(self):
        self.area()
class Square(Shape):
    def areaS(self):
        self.area()

#o=Shape(12,13)
m=Rect(2,4)
m.areaR()
s=Square(3,3)
s.areaS()
'''
    
