#_______Description_____

#https://projecteuler.net/problem=46
#It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
#9 = 7 + 2×12
#15 = 7 + 2×22
#21 = 3 + 2×32
#25 = 7 + 2×32
#27 = 19 + 2×22
#33 = 31 + 2×12
#It turns out that the conjecture was false.
#What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
##_______end_description_____:
from eulertools import Sieve #sieve of eratosthenes

def find_it(z):
    primes=Sieve(z);set_x=set()
    for i in primes:
        for n in range (1,i): #loop 1-prime
            x=i+(2*n**2);set_x.add(x) #calculate p+twice a square and add to set
            if x>z:break #break if exceeds
    for i in range(33,z,2): # until limit through odd
        if not any((i in primes,i in set_x)):return #check if prime or in set of generated items; if not for both return 
    return "Nothing within limit"

print(find_it(6000)) #keep checking limit
