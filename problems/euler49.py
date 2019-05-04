#_______Description_____

#https://projecteuler.net/problem=49
#The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
#There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
#What 12-digit number do you form by concatenating the three terms in this sequence?
##_______end_description_____:

from eulertools import Sieve
primes=Sieve(9999);check={}
def is_perm(n,d,z):
    if set(str(n))==set(str(d))==set(str(z)):return True
    else:return False
for i in primes:
    if i+3330 in primes and i+6660 in primes and i-1000>0:check[i]=(i+3330,i+6660)
print([str(i)+str(check[i][0])+str(check[i][1]) for i in check if is_perm(i,check[i][0],check[i][1]) and i!=1487])