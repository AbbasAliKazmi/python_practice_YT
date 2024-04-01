# List and Tuples


# fruits = ["apple", "banana", "cherry",]
# print(fruits[1])


#List slicing


# fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "grapes", "peach", "pear", "plum", "strawberry", "raspberry", "blueberry", "blackberry"]
# print(fruits[3:5])

#<.......neg slicing.......>

# fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "grapes", "peach", "pear", "plum", "strawberry", "raspberry", "blueberry", "blackberry"]
# print(fruits[-3:-1])


#list methods

#<.......append.......>
# fruits = ["apple", "banana", "cherry", "orange" ]
# fruits.append("blackberry")
# print(fruits)

#<.......sort.......>
# fruits = ["orange","apple", "cherry", "banana" ]
# fruits.sort()
# print(fruits)

# #<.......sort reverse.......>
# fruits = ["orange","apple", "cherry", "banana" ]
# fruits.sort(reverse=True)
# print(fruits)

#<.......list insert.......>
# fruits = ["orange","apple", "cherry", "banana" ]
# fruits.insert(2, "blackberry")
# print(fruits)

# #<.......list remove.......>
# fruits = ["orange","apple", "cherry", "banana" ]
# fruits.remove("cherry")
# print(fruits)


#<.......list pop.......>
# fruits = ["orange","apple", "cherry", "banana" ]
# fruits.pop(2)
# print(fruits)


#tuples
# tup = ( 5 , 7 , 8 , 9 , 10 )
# print(tup[4])
# print(type(tup))

#<.......tuple slicing.......>
# tup = ( 5 , 7 , 8 , 9 , 10 )
# print(tup[1:3])


#<.......tuple indexing.......>
# tup = ( 5 , 7 , 8 , 9 , 10 )
# print(tup[4])


#<.......tuple count.......>
# tup = ( 5 , 7 , 8 , 9 , 10 )
# print(tup.count(5))

#lets practice

# moviesplaylist = []

# moviesplaylist.append(str(input("Enter the name of the movie: ")))
# moviesplaylist.append(str(input("Enter the name of the movie: ")))
# moviesplaylist.append(str(input("Enter the name of the movie: ")))


# print(moviesplaylist)


#lets practice

# listgrades = ("A", "B", "C", "D", "E", "F" , "A" , "B" ,"E" , "C" , "A")

# print(listgrades.count("A"))


#lets practice 3

listgrades = ["A", "B", "C", "D", "E", "F" , "A" , "B" ,"E" , "C" , "A"]
listgrades.sort()
print(listgrades)