#_______Description_____

#https://projecteuler.net/problem=27
#Euler discovered the remarkable quadratic formula:
#$n^2 + n + 41$
#It turns out that the formula will produce 40 primes for the consecutive integer values $0 \le n \le 39$. However, when $n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41$ is divisible by 41, and certainly when $n = 41, 41^2 + 41 + 41$ is clearly divisible by 41.
#The incredible formula $n^2 - 79n + 1601$ was discovered, which produces 80 primes for the consecutive values $0 \le n \le 79$. The product of the coefficients, −79 and 1601, is −126479.
#Considering quadratics of the form:
#
#$n^2 + an + b$, where $|a| < 1000$ and $|b| \le 1000$where $|n|$ is the modulus/absolute value of $n$e.g. $|11| = 11$ and $|-4| = 4$
#
#Find the product of the coefficients, $a$ and $b$, for the quadratic expression that produces the maximum number of primes for consecutive values of $n$, starting with $n = 0$.
##_______end_description_____:

import functools
from functools import reduce

import time
start_time = time.time()

def Sieve(n): #Sieve of Eratosthenes
    out = []
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if (sieve[p]):
            out.append(p)
            for i in range(p, n+1, p):
                sieve[i] = False
    return out
primes=Sieve(1000)

@functools.lru_cache(None)
def isprime(n):   #similar to find factors function(problem 21) but checks if len is exactly 2- meaning number is prime. Works good enough for prime checking in this problem
            if n<=0:
                return False   
            if n%2==0:
                return False
            sumf=set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5)+1, 1) if not n % i)))
            if len(sumf)==2:
                return True

aa=0 ;bb=0;best=0 #scores
         
for a in range(-999,1000,2): #loop through coefficients a
    for b in primes: #loop through coefficients b - they must be primes since n=0 yields b
        n=0
        while True: #while result of below formula is prime, keep adding to the score n, otherwise break loop
            if isprime((n**2)+(a*n)+b):
                n+=1
            else:
                break
        if n>best:# update score and coefficients
            best=n;aa=a;bb=b
            
end_time=time.time()-start_time
print(end_time)                
print("Formula n**2%dn+%d, produces %d results that are primes for consecutive values of n, starting n=0"%(aa,bb,best),".Product of its cooeficients is %d"%(aa*bb))      



