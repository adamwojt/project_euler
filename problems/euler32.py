#_______Description_____

#https://projecteuler.net/problem=32
#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
#Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
#HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
##_______end_description_____:


# print(answer)
from itertools import permutations
digits=(1,2,3,4,5,6,7,8,9) 

perm2=list(permutations(digits)) #create list of all permutations

def checkproduct(perm):
    valid=set()
    for i in perm: #loop through permutations
        if (i[0]*10+i[1])*((i[2]*100)+(i[3]*10)+i[4])==(i[5]*1000)+(i[6]*100)+(i[7]*10)+i[8]:
            valid.add(i) # add to valid if format xx*xxx=xxxx satisfies
        if i[0]*((i[1]*1000)+(i[2]*100)+(i[3]*10)+i[4])==(i[5]*1000)+(i[6]*100)+(i[7]*10)+i[8]:
            valid.add(i)# add to valid if format x*xxxx=xxxx satisfies
    return valid

x=checkproduct(perm2)
answer=set()
for i in x:
    answer.add((i[5]*1000)+(i[6]*100)+(i[7]*10)+i[8]) #add product to answer

print(sum(answer))