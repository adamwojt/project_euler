#_______Description_____

#https://projecteuler.net/problem=47
#The first two consecutive numbers to have two distinct prime factors are:
#14 = 2 × 715 = 3 × 5
#The first three consecutive numbers to have three distinct prime factors are:
#644 = 2² × 7 × 23645 = 3 × 5 × 43646 = 2 × 17 × 19.
#Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
##_______end_description_____:


def Sieve(n): #modified Sieve to return how many times factor each number has
    factors={};sieve = [True] * (n+1)
    for p in range(2, n+1):
        if sieve[p]:
            for i in range(p,n+1,p):
                sieve[i]=False
                if i in factors:factors[i]+=1
                else:factors[i]=1
    return factors

factors=Sieve(150000);count=0 #i kept guessing the limit to find optimal solution- calculating Sieve takes most time
for i in range(210,500000): #loop through generated list and check when there are 4 occuring in row
    if factors[i]==4:count+=1
    else:count=0
    if count==4:print(i-3);break