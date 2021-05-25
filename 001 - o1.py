# Does not work!

import timeit

# slow
# simple loop
def loop(n):
    t = 0
    for i in range(1, n+1):
        if i % 3 == 0 or i % 5 == 0:
            t += i
    return t

# fast
# calculate each numbers' sum and subtract common multiplier
def calc(n):
    t03 = 3*(n/3)*(n/3+1)/2
    t05 = 5*(n/5)*(n/5+1)/2
    t15 = 15*(n/15)*(n/15+1)/2
    return t03 + t05 - t15

