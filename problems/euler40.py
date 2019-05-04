#_______Description_____

#https://projecteuler.net/problem=40
#An irrational decimal fraction is created by concatenating the positive integers:
#0.123456789101112131415161718192021...
#It can be seen that the 12th digit of the fractional part is 1.
#If dn represents the nth digit of the fractional part, find the value of the following expression.
#d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
##_______end_description_____:

from functools import reduce
string='';n=1
while len(string)<=999999: #create string of 12345..etc
    string+=str(n)
    n+=1

p=reduce(lambda x,y:x*y,[int(string[(10**n)-1]) for n in range(1,7)]) #find nth characters using reduce function
print(p)