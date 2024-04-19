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


class Movies:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        
    def type(self ):
        print("This is a movie", self.name)
        
        
m1 = Movies("Avengers", 2019)  
print(type)          
print(m1.name, m1.year)