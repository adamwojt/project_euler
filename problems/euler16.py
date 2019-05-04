#_______Description_____

#https://projecteuler.net/problem=16
#215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 21000?
##_______end_description_____:

import time
start_time = time.time()
score=0
for a in str(2**1000): # loop through digits of 2**1000
    score+=int(a) #add to score
print(score)

end_time=time.time()-start_time
print(end_time)