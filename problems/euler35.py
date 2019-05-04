#_______Description_____

#https://projecteuler.net/problem=35
#The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#How many circular primes are there below one million?
##_______end_description_____:

from eulertools import Sieve 
#Sieve of Eratosthenes                
primelist=set(Sieve(1000000))

for i in primelist.copy():
    for n in str(i):
        if int(n)==2 or int(n)==4 or int(n)==5 or int(n)==6 or int(n)==8 or int(n)==0:
#eliminate primes with numbers that cannot be ending of a prime number
            primelist.remove(i)
            break

answer={2,3,5,7}

for i in primelist:
    stri=str(i)
    perms=[stri[i:]+stri[:i] for i in range(len(stri))] #cyclic permutations list
    if all(int(i) in primelist for i in perms): #check if all permutations in list of primes
        answer.add(i)
        
print(len(answer))