# #<............function........>


# # def calc_sum(a,b):
# #     sum = a + b
# #     print(sum)
# #     return 
    
# # calc_sum(2,5)    

# # def num_avg( a, b, c):
# #     sum = a + b + c
# #     avg = sum / 3
# #     print(avg)
# #     return

# # num_avg(2,6,8)


# #<..............function types ............>
# # Built in functions                                User define function
# #  print()                                             jjo hum bnart hyn
# #   len()
# #   type()
# #   range()



# #<................Default parameters......>


# #lets practice


# # liist = [ 4,5,6,0,5,0]
# # heroes = ["thor" , "ironman" ,"spiderman" , "cap america"]


# # def len_list(list):
# #     print(len(list))

# # len_list(heroes)


# # def print_list(leest):
# #     for items in leest:
# #         print(items, end=" ")
                
# # print_list(heroes)        


# USD to PKR

# def converter(usd_val):
#     pkr_value = usd_val* 280
#     print(usd_val,"Dollars = ", pkr_value,"PKR")
    
# converter(5)  


#lets practice homework

def int_check(n):
    n = int(n)  # Convert input to integer
    if n % 2 == 0:
        print("Number is Even")
    else:
        print("Number is odd")

int_check(input("Enter a number: "))      