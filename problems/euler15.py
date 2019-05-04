#_______Description_____

#https://projecteuler.net/problem=15
#Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#
#
#How many such routes are there through a 20×20 grid?
##_______end_description_____:

import time
start_time = time.time()
import math

#Answers for any grid (n*n) will be central binomials of Pascal Triangle 
#or 2n factorial divided by n**2 factorial squared for n = size of grid (works for perfect squares only)

def central_binomals(n): 
    return (math.factorial(2*n))/(math.factorial(n))**2

print(central_binomals(20))

end_time=time.time()-start_time
print(end_time)