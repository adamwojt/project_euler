#_______Description_____

#https://projecteuler.net/problem=25
#The Fibonacci sequence is defined by the recurrence relation:
#Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
#Hence the first 12 terms will be:
#F1 = 1
#F2 = 1
#F3 = 2
#F4 = 3
#F5 = 5
#F6 = 8
#F7 = 13
#F8 = 21
#F9 = 34
#F10 = 55
#F11 = 89
#F12 = 144
#The 12th term, F12, is the first term to contain three digits.
#What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
##_______end_description_____:

import functools

@functools.lru_cache(None) #fib with cache approach
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

n=0
while len(str(fib(n)))<1000: #loop and stop at 1000 digits
    n+=1
print(n)

