# Project Euler - 1
# Attempting to generalise solution 
# Using Arithmetic Series Formulae

# Does not work !

import math

x = int(input("Input a number: "))
#a = int(input("Progression number: "))
user_input = input("Enter numbers split by a space: ").split()
int_user_input = [int(i) for i in user_input]
print(int_user_input)
hcf = math.gcd(*int_user_input)
array_a = []
total = 0

def calculate(x, int_user_input, TorF):
    global total
    if TorF == False:
        for a in int_user_input:

            nth_term = int(x/a) # since a = d always 
            last_term = int(a+(nth_term-1)*a)
            sumtotal = 0.5 * nth_term * ( a + last_term)
            array_a.append(sumtotal)
            total += sumtotal
        print("without decuct,", total)
        # alternatively, print((int(x/a)/2)*(a+a*int(x/a)))
    # if TorF == True:
    #         nth_term = int(x/hcf) # since a = d always 
    #         last_term = int(hcf+(nth_term-1)*hcf)
    #         hello = 0.5 * nth_term * ( hcf + last_term)
    #         print(hello)
    #         return (total - hello)
    if TorF == True:
        if hcf >
        nth_term = int(x/hcf) # since a = d always 
        last_term = int(hcf+(nth_term-1)*hcf)
        deduct = hcf*int(last_term/hcf)*(1+int(last_term/hcf))/2
        print("deductior,", deduct)
        total = total - deduct


calculate(x, int_user_input, False)
calculate(x, hcf, True)
print(total)

# ------------------------------------------------------------------------------------------------------ #

# More explanation of the calculate() function: 
# a + (n-1)d = x 
# rearrange to get n = (x-a)/d + 1
# since a = d, that simplifies to n = x/a 
# Use int() function to get rounding and therefore calculate the true last term:
# using a + (n-1) = L 
# Use 0.5*n*(a+L) = Σ


# ------------------------------------------------------------------------------------------------------ #

# Previous Version: 
# x = int(input("Input a number: "))
# a = int(input("Progression number: "))
# array_a = []

# def calculate(x,a):
#     nth_term = int(x/a) # since a = d always 
#     last_term = int(a+(nth_term-1)*a)
#     sumtotal = 0.5 * nth_term * ( a + last_term)
#     print(sumtotal)
#     # alternatively, print((int(x/a)/2)*(a+a*int(x/a)))




# calculate(x,a)

