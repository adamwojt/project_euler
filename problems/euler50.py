#_______Description_____

#https://projecteuler.net/problem=50
#The prime 41, can be written as the sum of six consecutive primes:
#41 = 2 + 3 + 5 + 7 + 11 + 13
#This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#Which prime, below one-million, can be written as the sum of the most consecutive primes?
##_______end_description_____:
from eulertools import Sieve,is_prime
primes=Sieve(5000)
def find_count(n):
    sump=0;i=n;prime=0
    while sump+primes[i+1]<10**6:
        sump+=primes[i];i+=1
        if is_prime(sump):prime=sump
    return prime
print(max([find_count(i) for i in range (10)]))