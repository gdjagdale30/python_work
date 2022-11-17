#Define a class in python

# class Person:
#     def __init__(self,name,sex,profession):
#         #data members (instance variable)
#         self.name=name
#         self.sex=sex
#         self.profession=profession
    
#     #Behavior(Instance methods)
#     def show(self):
#         print('Name: ',self.name,'Sex:',self.sex,'Profession',self.profession)

#     def work(self):
#         print(self.name,'working as a',self.profession)


# #Create object of class
# #Creation of object is called instantation

# jack=Person('jack','Male','software Engineer')

# jack.show()
# jack.work()



# class Employee:
#     "This is class Employee"
#     company_name='ABC Company'

#     #constructor to initialize the object
#     def __init__(self,name,salary):
#         #instance variable
#         self.name=name
#         self.salary=salary

#     def show(self):
#         print('Employee: ',self.name,self.salary,self.company_name)

# #create first object
# emp1=Employee("Harry",12000)
# emp1.show()

# class Student:
#     def __init__(self,name,perentage):  #>> Constructor with parameter of constructor
#         self.name=name    #Instance variable
#         self.percentage=perentage

#     def show(self):
#         print("Name is",self.name,"and percentage is",self.percentage)

# #Object of class

# s1=Student('Jessa',50)
# s2=Student('Jack',60)

# s1.show()
# s2.show()

#Working of destructor

# import time

# class Student:

#     #constructor
#     def __init__(self,name):
#         print("Inside Constuctor")
#         self.name=name

#     def show(self):
#         print("Hello,my name is",self.name)
#     #destructor
#     def __del__(self):
#         print("Object destroyed")

# s1=Student("Emma")
# s2=s1
# s1.show()

# #Delete object reference s1

# del s1

# time.sleep(2)
# print('After sleep')
# s2.show()


# import time


# class Vehicle():
#     def __init__(self, id, car):
#         self.id = id;
#         # saving reference of Car object
#         self.dealer = car;
#         print('Vehicle', self.id, 'created');

#     def __del__(self):
#         print('Vehicle', self.id, 'destroyed');


# class Car():
#     def __init__(self, id):
#         self.id = id;
#         # saving Vehicle class object in 'dealer' variable
#         # Sending reference of Car object ('self') for Vehicle object
#         self.dealer = Vehicle(id, self);
#         print('Car', self.id, 'created')

#     def __del__(self):
#         print('Car', self.id, 'destroyed')


# # create car object
# c = Car(12)
# # delete car object
# del c
# # ideally destructor must execute now

# # to observe the behavior
# time.sleep(8)


# class Vehicle:
#     def __init__(self, speed):
#         if speed > 240:
#             raise Exception('Not Allowed');
#         self.speed = speed;

#     def __del__(self):
#         print('Release resources')

# # creating an object
# car = Vehicle(350);
# # to delete the object explicitly
# del car


#Encapsulation
# class Employee:
#     def __init__(self,name,salary):
#         #Public member
#         self.name=name
#         #Private member
#         #Not accessible outside of class
#         self.__salary=salary

#     def show(self):
#         print("Name is ",self.name,"and salary is ",self.__salary)


# emp=Employee("Jessa",40000)
# emp.show()

# #Access salary from outside of class

# print(emp.__salary)

#Polymorphism

# class Circle:
#     pi=3.14

#     def __init__(self,redius):
#         self.redius=redius
    
#     def calculate_area(self):
#         print("Area of Circle :",self.pi*self.redius*self.redius) 

# class Rectangle:

#     def __init__(self,length,width):
#         self.length=length   
#         self.width=width

#     def calculate_area(self):
#         print("Area of Rectangle: ",self.length*self.width) 



# def area(shape):
#     shape.calculate_area()

# #Create object
# cir=Circle(5)
# rect=Rectangle(10,5)

# area(cir)
# area(rect)

#Inheritance
#Base Class
class Vehicle:

    def __init__(self,name,color,price):
        self.name=name
        self.color=color
        self.price=price

    def info(self):
        print(self.name,self.color,self.price)

#Child class

class Car(Vehicle):
    def change_gear(self,no):
        print(self.name,'change gear to number',no)


#Create object of car

car=Car("BMW X1","Black",35000)
car.info()
car.change_gear(5)
        

        