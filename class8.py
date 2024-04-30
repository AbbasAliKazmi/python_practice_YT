#<.................OOPS...........>


#Class and objects

# class Student:
#     name = "Ali"
    
# S1=Student()
# print(S1.name)   

#init method

# class Cars:
    
#     #default constructor
#     def __init__(self):
#         print("Car is added")
    
#     #parametarized constructor
#     name="Civic"
#     def __init__(self, otherCar , year):
#         self.name = otherCar
#         self.year = year
#         print("Car ia added")


# C1= Cars("Corola", 2019)
# print(C1.name, C1.year)     


#<............Class and Instance Attributes............>

# class CollegeStudent:
#     college = "FAST"
    
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year
#         self.college = "NUST"     #object level attribute>class level attribute
    
# s1 = CollegeStudent("Ali", 2019) 
# print(s1.name, s1.year, s1.college)   


#<............Class and Instance Methods............>


# class Movies:
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year
        
#     def type(self ):
#         print("This is a movie", self.name)
        
        
# m1 = Movies("Avengers", 2019)  
# print(type)          
# print(m1.name, m1.year)


#Lets Practice

# class Student:
#     def __init__(self, name , marks):
#         self.name = name
#         self.marks = marks
#         print("Student is added")
        
#     def get_avg(self):
#          sum = 0
#          for value in self.marks:
#              sum += value
#          print("Salam", self.name, "Your average is", sum/3)    
                

# s1=Student("Ali", [90, 80, 70])
# print(s1.name, s1.marks)
# s1.get_avg()


#<............Static Method/decorator............>decorator allows us to wrap another function in order to extend the behavior of the wrapped function, without permanently modifying it. 
#pory function ko leke uska behavior change kr k wapas dedeta h


#<................Two pillars of OOPs............>

#Abstraction    chupa hua

# class Car:
#     def __init__(self):
#         self.acc= False
#         self.clutch = False
#         self.brak= False
        
#     def start(self):
#         self.acc= True
#         self.clutch = True
        
# car1=Car()        
# car1.start()           


#Encapsulation    ek hi k andar sari chezen


# class Account:
#     def __init__(self, name , acc, balance):
#         self.name = name
#         self.acc = acc
#         self.balance = balance
        
#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs", amount, "has been debited from your account")
#         print("Hey" , self.name,"Your remaining balance is", self.get_balance())    
    
#     def credit(self, amount):
#         self.balance += amount
#         print("Rs", amount, "has been credited to your account")
#         print("Hey" , self.name,"Your new balance is", self.get_balance())
        
#     def get_balance(self):
#         return self.balance
    
# c1=Account("Ali", 1234, 50000)
# c1.debit(500)
# c1.credit(200)

class Car:
    def __init__(self, name , model, year):
        self.name = name
        self.model = model
        self.year = year
        self.speed = 0
        
    def accelerate(self, increment):
        self.speed += increment
        print("The", self.name, self.model, "is accelerating. Current speed:", self.speed)
        
    def brake(self, decrement):
        if self.speed >= decrement:
            self.speed -= decrement
            print("The", self.name, self.model, "is braking. Current speed:", self.speed)
        else:
            print("The", self.name, self.model, "is already stopped.")
        
    def get_speed(self):
        return self.speed
    
c1=Car("Honda", "Civic", 2019)
c1.accelerate(20)
c1.brake(10)


