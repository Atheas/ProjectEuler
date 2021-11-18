# Project Euler - Problem 2
#  I think it works. 

n1 = 1
n2 = 2
temp = 0
total_even = 0

def fibonacci(n1, n2):
       global total_even 
       temp = n1 + n2
       if n2 % 2 == 0:
           total_even += n2 
       n1 = n2
       n2 = temp
       return temp, n1, n2

def call(n1, n2, temp):
    while temp < (4*10**6): # total number should be 4*10**6 (million)
        temp, n1, n2 = fibonacci(n1, n2)

call(1,2, temp)
print(total_even)
