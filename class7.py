#<......................FILE I/O............>



#File open and close

# f = open("democlass7.txt", "r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

# #File open and read with characters 

# f = open("democlass7.txt", "r")
# data = f.read(10)
# print(data)
# print(type(data))
# f.close()

#File open and read with line by line using .readine 

# f = open("democlass7.txt", "r")
# line1 = f.readline()
# print(line1)
# print(type(line1))
# f.close()


# how to write(overwrite) in a file

# a = open("democlass7.txt" , "w")
# a.write("Changing the line")
# a.close()

#how to append(add into previous one) in a file

# a = open("democlass7.txt" , "a")
# a.write("adding the new line")
# a.close()

#how to append(add into previous one) in a file on next line add \n

# a = open("democlass7.txt" , "a")
# a.write("\n will add to new line")
# a.close()

#how to append(add into previous one) in a file on next line add \n

# a = open("democlass7.txt" , "w")
# a.write("\n will add to new line")
# a.close()

# how to directly create a new file 

a = open("sample.txt","w")
a.close