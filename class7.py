#<......................FILE I/O............>



#File open and close

f = open("democlass7.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()

#File open and read with characters or by line

f = open("democlass7.txt", "r")
data = f.read(10)
print(data)
print(type(data))
f.close()