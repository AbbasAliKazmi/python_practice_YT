# from fastapi import FastAPI

# app = FastAPI(title="Hello World API", 
#     version="0.0.1",
#     servers=[
#         {
#             "url": "http://0.0.0.0:8000", # ADD NGROK URL Here Before Creating GPT Action
#             "description": "Development Server"
#         }
#         ])


# @app.get("/")
# def read_root():
#     return {"Message": "Hello World"};

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}


# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))

# sum = a + b
# print(sum)

# input from users
# first = str(input("Enter your name: "))
# second = str(input("Enter your last name: "))

# print(f"Hello {first} {second}!")



# input and output according to users if elses
# age = int(input("Enter your age: "))

# if (age >= 18):
#     print("You are an adult")
# elif (age >= 13):
#     print("You are a child")
# elif (age >= 3):
#     print("You are a baby")
# else:
#     print("You are an animal")    


# opertaors with input and if else

# num = int(input("enter a num: "))
# rem = num % 2 
# if rem == 0:
#     print("The number is even")
# else:
#     print("The number is odd")    



# opertaors with input and if else
# x = int(input("Enter a number: "))

# if(x % 7 == 0):
#     print("The number is divisible by 7")
# else:
#     print("The number is not divisible by 7") 



# List and Tuples

fruits = ["apple", "banana", "cherry"]
print(fruits)
print(type(fruits))



cars = ["bmw" , "mercedes" , "ferrari"]
print(cars)
print(types(cars))