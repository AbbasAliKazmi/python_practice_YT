#<......................FILE I/O............>



#File open and close

f = open("democlass7.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()