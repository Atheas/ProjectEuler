# Project Euler
# 1 - Multiples of 3 and 5

total_num_3 = 0
total_num_5 = 0
final_3 = 0
final_5 = 0
number = 0

n = int(input("Input a number: "))


def TakeMult3(number, total_num_3):
    while number < n: 
       number += 3 
       total_num_3 += number
       final_3 = total_num_3 - number #Take last number before exceeding n
    print("Sum of multiples of 3:", final_3)

def TakeMult5(number, total_num_5):
    while number < n:
        number += 5
        total_num_5 += number
        final_5 = total_num_5 - number
    print("Sum of multiple of 5:", final_5)

        
TakeMult3(number, total_num_3)
TakeMult5(number, total_num_3)

