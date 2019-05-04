#_______Description_____

#https://projecteuler.net/problem=41
#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
#What is the largest n-digit pandigital prime that exists?
##_______end_description_____:

#only 4 and 7 digit pandigital numbers can be prime because otherwise sum of all digit is divisble by 3 meaning whole number
#is divisible by 3. That's why limit is largest pandigital 7-digit number.

from eulertools import is_prime,is_pandigital 
 
for n in range(7654321,1,-2): # looping down, decrementing by 2
    if is_pandigital(n):
        if is_prime(n):
            print(n)
            break

