#_______Description_____

#https://projecteuler.net/problem=48
#The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
#Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
##_______end_description_____:

import time
start_time = time.time()

total=str(sum([i**i for i in range(1,1000)]));print(total[-10:]) #self exploratory one-liner

end_time=time.time()-start_time
print(end_time)