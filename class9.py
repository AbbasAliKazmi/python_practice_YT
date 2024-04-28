#<...................OOPS Part 2...............>


#del keyword     to delete the object or its attribute

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        

# s1 = Student("John", 20)
# print(s1.name)    

# del s1.name
# print(s1.name)        


#private attribute and methods   (__ laga dia to private ho jata hai , function k bagar access nahi hota)

# class Account:
#     def __init__(self, acc_no, acc_passw):
#         self.acc_no = acc_no
#         self.__acc_passw = acc_passw
        
# acc1 = Account(101, "abcs")
# print(acc1.acc_no.__acc_passw)        



#<................Inheritance...............>


#Single inheritance

# class Car:
#     @staticmethod
#     def start():
#         print("Car started...")
        
#     @staticmethod
#     def stop():
#         print("Car stopped...")
        
# class Toyota(Car):
#     def __init__(self, name):
#         self.name = name
        
# c1 = Toyota("Toyota")
# print(c1.name)
# print(c1.start())


#Multi level inheritance   (ek class dusri class k ander or dusri class teesri class k ander)


# class Car:
#     @staticmethod
#     def start():
#         print("Car started...")
        
#     @staticmethod
#     def stop():
#         print("Car stopped...")
        
# class Toyota(Car):
#     def __init__(self, brand):
#         self.name = brand
        
# class Fortuner(Toyota):
#     def __init__(self, type):
#         self.name = type
        
# car1=Fortuner("SUV")    
# car1.start()    


#Multiple inheritance   (ek new class 2 parent ya derive class se inherit karta hai)

# class A:
#     varA="Welcome to class A"
    
# class B:
#     varB="Welcome to class B"
    
# class C(A,B):
#     varC="Welcome to class C"
    
# c1=C()

# print(c1.varA)
# print(c1.varB)
# print(c1.varC)
            
            
#<..................Super Method...............>            
#(super method se parent class k constructor or methods ko call kar sakte hain)

# class Car:
#     def __init__(self, type):
#         self.type = type
        
#     @staticmethod
#     def start():
#         print("Car started...")
        
#     @staticmethod
#     def stop():
#         print("Car stopped...")    
        
# class Toyota(Car):
#     def __init__(self, name ,type):
#         super().__init__(type)
#         self.name = name
        
        
# car1=Toyota("SUV", "electriv")    
# print(car1.type)


#Class Method
 
# class Person:
#     name="anonymous"
    
#     def changeName(self,name):
#         self.name=name

# p1=Person()
# p1.changeName("John")
# print(p1.name)    
# print(Person.name)    


#is tareekay sy class k attribute change ni hua,nea attribute ban gaya hai
#<.......x..................x.................x...............>

#1st indirect method class attribute ko chang karne ka lie


# class Person:
#     name="anonymous"
    
#     def changeName(self,name):
#         Person.name=name

# p1=Person()
# p1.changeName("John")
# print(p1.name)    
# print(Person.name)  

#2nd indirect method class attribute ko chang karne ka lie __class__ use kar k

# class Person:
#     name="anonymous"
    
#     def changeName(self,name):
#         self.__class__.name=name

# p1=Person()
# p1.changeName("John")
# print(p1.name)    
# print(Person.name)  

#<...........x......................x..................x.....................x......>

#Actual Class Method

#yahan @classmethod laga k hum directtly class attribute change kar skty hyn

# class Person:
#     name="anonymous"
    
#     @classmethod
#     def changeName(cls,name):
#         cls.name=name

# p1=Person()
# p1.changeName("John")
# print(p1.name)    
# print(Person.name) 


#<...........x......................x..................x.....................x......>
#<................Property Decorator...............>

# class Student:
#     def __init__(self, phy, chem, math) :
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#         self.percentage = str((self.phy + self.chem + self.math) / 3)+"%"

# st1=Student(50,60,70)
# print(st1.percentage)


# st1.phy=86
# print(st1.percentage)

#yahan ub percentage update nahi hua, is ka solution property decorator hai

#<...................x..................x..................x..................x...............>

# neche jo kam hy ye b ho sakta tha par better tareka hy @property decorator use krna


# class Student:
#     def __init__(self, phy, chem, math) :
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#         self.percentage = str((self.phy + self.chem + self.math) / 3)+"%"
        
        
#     def calcPercentage(self):
#         self.percentage=str((self.phy + self.chem + self.math) / 3)+"%"    

# st1=Student(50,60,70)
# print(st1.percentage)


# st1.phy=86
# print(st1.phy)
# st1.calcPercentage()
# print(st1.percentage)


#<...................x..................x..................x..................x...............>
#@property ki help sy value ek new updated attribute me convert hojaegi

# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
        
#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.math) / 3) + "%"

# st1 = Student(50, 60, 70)
# print(st1.percentage)

# st1.phy = 86                                              #marks change krty hi @property method sy khud hi value update hojaegi
# print(st1.percentage)



#<...................x..................x..................x..................x...............>
#<...................Polymorphism...............>


# class Complex:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag
        
#     def ShowNum(self):
#         print(self.real, "i +", self.imag, "j")
        
# n1 = Complex(3, 4)
# n1.ShowNum()

# n2 = Complex(5, 6)
# n2.ShowNum()

#<...................x..................x..................x..................x...............>
#yahan hum apny complex numbers ko add krny k  lie dunder function s use krty hyn

#<.......................Operators and dunder functions..................>

# class Complex:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag
        
#     def ShowNum(self):
#         print(self.real, "i +", self.imag, "j")
        
#     def add(self, other):
#         newReal=self.real + other.real
#         newImag=self.imag + other.imag
#         return Complex(newReal, newImag)    
        
# n1 = Complex(3, 4)
# n1.ShowNum()

# n2 = Complex(5, 6)
# n2.ShowNum()

# n3 = n1.add(n2)
# n3.ShowNum()

#par yahan me nai chahta k n3 me add kron phr n2 likhon, me chahta hon k n3 + n2 likhon to ye hojaye

#<...................x..................x..................x..................x...............>

# class Complex:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag
        
#     def ShowNum(self):
#         print(self.real, "i +", self.imag, "j")
        
#     def __add__(self, other):                  #__add__  lagany sy ye dunder function add k lie use hojata hai 
#         newReal=self.real + other.real
#         newImag=self.imag + other.imag
#         return Complex(newReal, newImag)    
        
#     def __sub__(self, other):                  #__sub__  lagany sy ye dunder function sub k lie use hojata hai 
#         newReal=self.real - other.real
#         newImag=self.imag - other.imag
#         return Complex(newReal, newImag)  
    
#     def __mul__(self, other):                  #__mul__  lagany sy ye dunder function multiply k lie use hojata hai 
#         newReal=self.real * other.real
#         newImag=self.imag * other.imag
#         return Complex(newReal, newImag)
       
        
# n1 = Complex(3, 4)
# n1.ShowNum()

# n2 = Complex(5, 6)
# n2.ShowNum()

# n3 = n1 + n2
# n3.ShowNum()

# n4=n1-n2
# n4.ShowNum()

#getter function

# def get_real(self):
#     return self.real

# def get_imag(self):
#     return self.imag

# def get_complex_number(self):
#     return f"{self.real}i + {self.imag}j"

# def add_complex_numbers(self, other):
#     new_real = self.real + other.real
#     new_imag = self.imag + other.imag
#     return Complex(new_real, new_imag)

# def subtract_complex_numbers(self, other):
#     new_real = self.real - other.real
#     new_imag = self.imag - other.imag
#     return Complex(new_real, new_imag)

# def multiply_complex_numbers(self, other):
#     new_real = self.real * other.real
#     new_imag = self.imag * other.imag
#     return Complex(new_real, new_imag)

#Setters function

def set_real(self, value):
    self.real = value

def set_imag(self, value):
    self.imag = value

def set_complex_number(self, real, imag):
    self.real = real
    self.imag = imag

def set_complex_number_from_string(self, complex_str):
    parts = complex_str.split("+")
    real = int(parts[0].strip())
    imag = int(parts[1].strip().replace("j", ""))
    self.real = real
    self.imag = imag