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

# a = open("sample.txt","w")
# a.close

#how to open ,read it and write it

# a = open("sample.txt" , "r+")
# a.write("This is a new text")
# a.close

#File input and output with syntax

# with open("sample.txt","r") as t:
#     data=t.read()
#     print(data)

#<..............Deleting a file........>


#to delete a whole file

# import os

# os.remove("sample.txt")


#"with" method with a word finding function

# word = "sample"
# with open("sample.txt", "r") as q:
#     data = q.read()
#     if(data.find(word) != -1):
#         print("Found")
#     else:
#         print("Not Found")    
        
        

#function of finding a word in a line by line

def  check_for_line():
    word = "BSCS"
    data = True
    line_no = 1
    with open("sample.txt" , "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1    
    
    return -1   


check_for_line()     