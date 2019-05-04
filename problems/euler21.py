#_______Description_____

#https://projecteuler.net/problem=21
#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#Evaluate the sum of all the amicable numbers under 10000.
##_______end_description_____:
import time
start_time = time.time()

#below function returns sum of list of all factors. checking only up to sqrt(n) since smallest prime factor is 2

def factors(n): 
        return sum(i+(n//i) for i in range(1, int(n**(.5)), 1) if not n%i)-n

# to visualise below is return of 'list([i,(n//i)] for i in range(1, int(n**(.5)), 1) if not n%i)' for n=100:
#[[1, 100], [2, 50], [4, 25], [5, 20]] 
#as we can see, in original function we are returning list of sums 101,52,29,25. we then need to substract 100 to get sum of 'proper' divisors.

def finder(limit): 
    total={}
    for i in range(1,limit,1): #loop to limit
        total[i]=factors(i) #add to dictionary key=number, value= sum of factors
    return sum(n for n,i in total.items() if n!=i and total.get(i)==n)  
    #return sum all amicable numbers. skip situations where sum of factors is same as number(perfect number).

print(finder(10000))

     
end_time=time.time()-start_time
print(end_time)

start_time = time.time()



