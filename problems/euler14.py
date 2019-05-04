#_______Description_____

#https://projecteuler.net/problem=14
#The following iterative sequence is defined for the set of positive integers:
#n → n/2 (n is even)n → 3n + 1 (n is odd)
#Using the rule above and starting with 13, we generate the following sequence:
#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#Which starting number, under one million, produces the longest chain?
#NOTE: Once the chain starts the terms are allowed to go above one million.
##_______end_description_____:

import time
start=time.time()

cache = {1:1,2:1} #cache with saved steps for performance
def collatz(n):
    if n not in cache: #check if not in cache
        if n % 2 == 0: # if even do 1+ recursion for even :
            cache[n] = 1 + collatz(n / 2)
        else: #if odd do 1+ recursion for odd
            cache[n] = 1 + collatz(3 * n + 1)
    return cache[n] #return cache[n]

num=0;greatest=0

for n in range(1,10**6): #loop to milion
    c=collatz(n)
    if num<c: #update score of steps and number if score bigger than current
        num=c
        greatest=n

print('{0} has {1} elements. calculation time ={2} seconds.'.format(greatest,num,time.time()-start))