#_______Description_____

#https://projecteuler.net/problem=3
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
##_______end_description_____:


def prime_factors(n):
    factors=[]
    d=2
    while(d*d<=n): #make sure d^2 doesn't exceed number
        while(n>1): #until 1         
            while n%d==0: #until divisible by prime
                factors.append(d)
                n=n/d
            d+=1 #move to next number, can be improved by only looping through primes numbers but is quick enough in this case.
    return factors

factors=prime_factors(600851475143)
print(factors)
