#_______Description_____

#https://projecteuler.net/problem=7
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?
##_______end_description_____:
#VERY SLOW- first solution
primes=[]


for num in range(2,10**20):
    if all(num%i!=0 for i in range(2,num)):
        primes.append(num)
    if len(primes)== 10001:
        break
   
print(primes[10000])

#Faster- checking sqrt(num)
# import time
# start_time=time.time()
# 
# import math
# for num in range(3,10**10,2):
#     if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
#         primes.append(num)
#     if len(primes)== 10001:
#         break
# 
# 
# print(primes[10000])
# 
# end_time=time.time()-start_time
# print(end_time)


