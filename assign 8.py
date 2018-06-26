'''
ASSIGNMENT-8
Classes and Modules I

Let’s have some fun with classes and objects.
1.	Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.

2.	Create a Student class and initialize it with name and roll number. Make methods to :
●	Display - It should display all informations of the student.

      3. Create a Temprature class. Make two methods :
●	 convertFahrenheit - It will take celsius and will print it into Fahrenheit.
●	 convertCelsius - It will take Fahrenheit and will convert it into Celsius.
   **  4. Create a class MovieDetails and initialize it with Movie name , artistname,Year of release and ratings.
Make methods to 
●	Display-Display the details.
●	Update- Update the movie details.

5. Create a class Expenditure and initialize it with expenditure,savings.Make the following methods.
●	 Display expenditure and savings
●	Calculate total salary
●	Display salary
         



'''










'''
class circle():
    def __init__(self,radius):
        self.radius=radius
    def getArea(self):
        print("Area of circle : ",3.14*self.radius*self.radius)
    def getCircumference(self):
        print("Circumference : ",2*3.14*self.radius*self.radius) 

ob=circle(5)
ob.getArea()
ob.getCircumference()


class Student():
    def __init__(self,name="nupur",rollno=21):
        self.name=name
        self.rollno=rollno
    def display(self):
        print(self.name)
        print(self.rollno)

ob1=Student()
ob1.display

class Temperature():
    def ConvertFahrenheit(self):
        self.c=int(input("Enter Celsius: "))
        print("Fahrenheit is",self.c*1.8+32,"F")

    def ConvertCelsius(self):
        self.f=int(input("Enter Fahrenheit: "))
        print("Celsius is",(self.f-32)/1.8,"C")
ob2=Temperature()
ob2.ConvertFahrenheit()
ob2.ConvertCelsius()

class MovieDetails():
    def Enternew(self):
        self.m_name=input("\n Enter movie name : ")
        self.m_artist=input("\n Enter movie artist : ")
        self.m_year=int(input("\n Enter movie year : "))
        self.m_ratings=input("\n Enter movie ratings : ")

    def Display(self):
        print("\n movie name : ",self.m_name)
        print("\n movie artist : ",self.m_artist)
        print("\n movie year : ",self.m_year)
        print("\n movie ratings : ",self.m_ratings)

    def Update(self):
        MovieDetails.Enternew(self)

ob3=MovieDetails()

class Expenditure():
    def Enternew(self):
        self.expenditure=int(input("\n Enter expenditure : "))
        self.savings=int(input("\n Enter savings : "))
    def Display(self):
        print("\n Expenditure is : ",self.expenditure)
        print("\n Savings is : ",self.savings)
    def TotalSalary(self):
        self.total=self.expenditure+self.savings
    def DisplaySalary(self):
        print(self.total)
        
ob4=Expenditure()
'''
