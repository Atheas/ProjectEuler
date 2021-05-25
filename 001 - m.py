# Project Euler - 1

number_3 = 0
number_5 = 0
total_3 = 0
total_5 = 0

number_15 = 0 # Lowest common divisor
total_15 = 0
count = 0

n = 1000 

while (number_3 <= n):
    number_3 += 3 
    total_3 += number_3

while (number_5 < n):
    number_5 += 5
    total_5 += number_5

while number_15 <= n: # Multiples of 15 are where 3 and 5 have common terms so find sum
    number_15 += 15 
    total_15 += number_15
        
total_5 = total_5 - number_5
total_3 = total_3 - number_3
total_15 = total_15 - number_15

final = (total_3 + total_5) - total_15 # Take away sum of multiples of 15
print(final)
