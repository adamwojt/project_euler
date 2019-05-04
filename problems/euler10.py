#_______Description_____

#https://projecteuler.net/problem=10
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.
##_______end_description_____:
import time
start_time = time.time()

#Sieve of Eratosthenes

def Sieve(n):
    out = []
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if (sieve[p]):
            out.append(p)
            for i in range(p, n+1, p):
                sieve[i] = False
    return out
print(sum(Sieve(2*10**6)))


end_time=time.time()-start_time
print(end_time)
