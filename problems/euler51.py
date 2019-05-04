#_______Description_____

#https://projecteuler.net/problem=51
#By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
#By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.
#Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
##_______end_description_____:
from eulertools import Sieve,is_prime
primes_set=set(Sieve(999999));primes_reduce=set()
for i in primes_set:
    if i>100000:
        digits=[n for n in str(i)]
        for n in digits:
            if digits.count(n)==3 and n!=digits[5] and any((n=='0',n=='1',n=='2')):primes_reduce.add(i)
            
for i in primes_reduce:
    digits=str(i);count=0
    for n in digits:
        if digits.count(n)==3:repeating=n;break
    for d in range(0,10):
        new_prime=int(digits.replace(repeating,str(d),3))
        if is_prime(new_prime) and new_prime>100000:count+=1
    if count==8:print(i);break