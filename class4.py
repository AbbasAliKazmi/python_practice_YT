#Dictionary

# info ={
#     "name": "John",
#     "age": 25,
#     "gender": "male"
# }

# print(info)

#<........nested dictionary..........>

# info ={
#     "name": "John",
#     "age":  65,
#     "subject" :{
#         "math": 90,
#         "science": 80
#     }
# }    
# print(info)


#Dictionary Methods

#<..........key method..........>


# info ={
#     "name": "John",
#     "age":  65,
#     "subject" :{
#         "math": 90,
#         "science": 80
#     }
# }

# print(info.keys())


#<..........values method..........>

# info ={
#     "name": "John",
#     "age":  65,
#     "subject" :{
#         "math": 90,
#         "science": 80
#     }
# }

# print(info.values())


#<..........items method..........>
# means it will return the key and value pair
 
# info ={
#     "name": "John",
#     "age":  65,
#     "subject" :{
#         "math": 90,
#         "science": 80
#     }
# }

# print(info.items()) 



#<..........get method..........>

# info ={
#     "name": "John",
#     "age":  65,
#     "subject" :{
#         "math": 90,
#         "science": 80
#     }
# }

# print(info.get("age"))

#<..........update method..........>

# info ={
#     "name": "John",
#     "age":  65,
#     "subject" :{
#         "math": 90,
#         "science": 80
#     }
# }

# info.update({"nam": "Smith"})
# print(info)



#Sets in Python


#<..........set..........>
# jisme 1 value{} 1 hi bar store hogi, with no order or indexing


# cars = {"bmw", "audi", "ford"}

# print(cars)
# print(type(cars))
# print(len(cars))

#<..........empty set..........>

# cars = set()
# print(cars)


#set methodss

#<..........add method..........>

# cars = { "bmw", "audi", "ford"}

# cars.add("lambo")
# print(cars)



#<..........remove method..........>

# cars = { "bmw", "audi", "ford" , "lambo"}

# cars.remove("audi")
# print(cars)


#<..........clear method..........> set ko khali krny k liye

# cars = { "bmw", "audi", "ford" , "lambo"}
# cars.clear()
# print(cars)


#<..........pop method..........> set me sy koi b random value remove krny k liye

# cars = { "bmw", "audi", "ford" , "lambo"}
# print(cars.pop())


#<..........union method..........> 2 sets ko combine krny k liye maths ki union k tarah

# set1 = {1,2,3,4,5}
# set2={2,8,1,6,9,5,3}

# print(set1.union(set2))


#<..........intersection method..........> 2 sets me sy common values ko return krny k liye


# set1 = {1,2,3,4,5}
# set2={2,8,1,6,9,5,3}

# print(set1.intersection(set2))



#Lets do some practice


#store the meaning of words in a dictionary

# wordsMeaning = {
#     "cat" : "a cute animal",
#     "dog" : "a faithful animal",
#     "apple" : ["a red fruit" , "a company"]
# }

# print(wordsMeaning)



#storing the input values in a dictionary



subjects = {}

physics = input("Enter your physics marks: ")
chemistry = input("Enter your chemistry marks: ")
math = input("Enter your math marks: ")
history = input("Enter your history marks: ")

subjects.update({"physics": physics})
subjects.update({"chemistry": chemistry})
subjects.update({"math": math})
subjects.update({"history": history})

print(subjects)