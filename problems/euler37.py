#_______Description_____

#https://projecteuler.net/problem=37
#The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
#Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
##_______end_description_____:
from eulertools import Sieve
#Sieve of Eratosthenes                
primelist=set(Sieve(1000000))

for i in primelist.copy():
    for n in str(i):
        if len(str(i))<2:
            primelist.remove(i)
            break
        if int(n)>100 and (int(n)==2 or int(n)==4 or int(n)==5 or int(n)==6 or int(n)==8 or int(n)==0):
#eliminate primes with numbers that cannot be ending of a prime number
            primelist.remove(i)
            break
answer=set()
primelistraw=set(Sieve(1000000))
for i in primelist:
    cuts=[]
    for n in range(1,len(str(i))):
        cuts.append(str(i)[n:])
        cuts.append(str(i)[:n])
    if all(int(i) in primelistraw for i in cuts): #check if all permutations in list of primes
        answer.add(i)
        
print(sum(answer))
