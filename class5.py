#<................Loops................>


#<....while loop....>
# c = 1
# while c <= 5:
#     print("hello")
#     c += 1
    
    
#<....while loop with print iterator....>
# c = 1
# while c <= 5:
#     print("hello" , c)
#     c += 1


#<....while loop with numbers....>
# c = 1
# while c <= 5:
#     print( c)
#     c += 1



#Lets print 1 to 100 numbers
# i=1
# while i <=100 :
#     print(i)
#     i += 1


#Lets practice 10 to 1 numbers
# i =10
# while i >=1:
#     print(i)
#     i -= 1


#Lets practice number n multiplication
# i=1
# while i <= 10:
#     print(3*i)
#     i += 1
    
 
#lets practice loop with input from user

# i=1
# n = int(input("Enter number:"))
# while i <= 10:
#     print(n*i)
#     i += 1    


#Lets practice with list n loops

# n = [ 13, 24, 32,34,57,6,17,38,93,10 ]
# idx = 0
# while idx < len(n):
#     print(n[idx])
#     idx += 1

#Lets practice finding number in tuple

# nums = ( 3, 4, "v",6 ,1 ,"h" ,6 ,"m" )
# x = 6
# i =0
# while i < len(nums):
#     if(nums[i] == x):
#         print("found at ", i)
#     i += 1
    
    
    
#<................Loops Break and Continue................>

#break
# a = 1
# while a <= 5:
#     print(a)
#     if(a == 3):
#         break
#     a += 1
    
    
#continue

# a = 1
# while a <= 5:
#     if(a == 3):
#         a +=1
#         continue
#     print(a)
#     a += 1    
    
    
#<................For Loops ................>

# madarsa = ["Ali", "Saad", "Usama", "Dani"]
# for students in madarsa:
#     print(students)  
    
#<.......str in for loops.......>

# str = "Abbas"
# for a in str:
#     print(a) 
    
  
#<....... for loops with else.......>

# madarsa = ["Ali", "Saad", "Usama", "Dani"]
# for students in madarsa:
#     print(students) 
# else:
#     ("End of code")            

#Lets Practice

# nums = (2, 5, 8, 98, 45, 63, 7, 65)
# x= 63
# i=1

# for n in nums:
#     if( n == x):
#         print("num is found at idx:", i)
#     i += 1


#<................range................>

# seq= range(5)   #single value means stop value

# for i in seq:
#     print(i)

# for i in range(3,12):  #double val means start and stop val
#     print(i)
    

# for i in range(3,12, 2):  #triple val means start and stop and steps val
#     print(i)    



#Lets Practice

#forward
# for i in range(1,101):
#     print(i)


#backward
# for i in range(100 ,0 ,-1):
#     print(i)

#n number multiplication

# n = int(input("Enter a number: "))
# for i in  range(1,10):
#     print(n*i)



#<................pass statement................> jab koi kam ni krana


# for i in range(2,10):
#     pass

# print("Hello000000000000")    


#lets practice

# n =10
# sum=0
# for i in range(1, n+1):
#     sum += i

# print("Total numbers of sum is :", sum)

#lets practice using while


n=7
sum=0
i=1

while i <= n:
    sum += i
    i +=1

print(sum)

a="Abba"
b="Ali"
c="Kazmi"

My_name_is= a+b+c
print(My_name_is)