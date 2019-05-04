#_______Description_____

#https://projecteuler.net/problem=4
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.
##_______end_description_____:

import time
start_time = time.time()
def is_palindrome(s): # check if palindrome recursive style
    if s== '':
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False


answer=set()
for i in range(100,999): #loop 100-999 
    for n in range(i,999): #loop number-999
        x=str(i*n) 
        if is_palindrome(x):#check if palindrome
            answer.add(int(x))
print(max(answer))

