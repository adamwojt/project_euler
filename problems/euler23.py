#_______Description_____

#https://projecteuler.net/problem=23
#A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
##_______end_description_____:

import time
start_time = time.time()

def sumf(n): #same function as in problem 21 but added checkpoint to check when sum exceeds number itself
        sumf=sum(i+(n//i) for i in range(1, int(n**(.5)), 1) if not n%i)-n
        if sumf>n:
            return True

abu=set(n for n in range(1,28112) if sumf(n)) # set of all abundant numbers up to limit given in problem

def checksum(n):
    for i in abu: #loop through set
        if n-i in abu:  # if difference in set
            return True
        elif i*2>n: #if i is twice than n - no need to check. ex. n=50, i = 26, n-i=24, we already checked 50-24 =26  
            return False

answer=sum(i for i in range(1,28124) if not checksum(i)) #loop to limit and sum
print(answer)

end_time=time.time()-start_time
print(end_time)



