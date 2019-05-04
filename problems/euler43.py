#_______Description_____

#https://projecteuler.net/problem=43
#The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
#Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
#d2d3d4=406 is divisible by 2
#d3d4d5=063 is divisible by 3
#d4d5d6=635 is divisible by 5
#d5d6d7=357 is divisible by 7
#d6d7d8=572 is divisible by 11
#d7d8d9=728 is divisible by 13
#d8d9d10=289 is divisible by 17
#Find the sum of all 0 to 9 pandigital numbers with this property.
##_______end_description_____:

import time
start_time = time.time()
   
start=[]
def find_sum(n):
    if not n: #generate endings that divide by 17 and have no repeated digits
        for i in range(102,988):
            if len(set(str(i)))==3 and int(str(i)[0:3])%17==0:
                start.append(i)
    leng=len(str(n[0]))  #length of current cycle          
    if leng==10: #once reach 10, return sum of all
        return sum([int(i) for i in n])
    divideby=[13,11,7,5,3,2,1] #list of primes to divide by(1 is not a prime!)
    newlist=[]
    for i in n: #add digit and check if no repeated digits and divisible by current prime for given leng.
        for n in range(0,10):
            new=str(n)+str(i)
            if len(set(str(new)))==leng+1 and int(str(new)[0:3])%divideby[leng-3]==0:
                newlist.append(new)
    return find_sum(newlist) # recursion

print(find_sum(start))
  
   
end_time=time.time()-start_time
print("{0}ms".format((time.time() - start_time) * 1000))
