#_______Description_____

#https://projecteuler.net/problem=24
#A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
#012   021   102   120   201   210
#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
##_______end_description_____:


#For n digits, there are n! = (1*2*..n) permutations
# This means that there are (n-1)! permutations per starting digit.
# So to determine the index of the first digit, we must do an integer divison of 999999//9!
# Then we must take the rest of the division as an new limit for the group of remaining digits.
# Continue until there remains only one digit.

from math import factorial as f

def find_perm(limit,list_digits=[0,1,2,3,4,5,6,7,8,9],answer=''): #set default answer as blank and list of digits as 0-9 
	working_copy=list_digits.copy()
	n=len(list_digits)-1 #len of list
	per_digit=f(n) #calculate factorial of remaining digits
	if limit+1>f(n+1): #check if limit is more than possibile permutations(not needed in actual problem)
		return "Limit exceeds number of permutations. Max: %d"%(f(n+1)-1)
	digit=working_copy.pop(limit//per_digit) #calculate digit by floor division by possible permutations
	answer+=str(digit) # append answer with digit
	new_limit=limit%per_digit #calculate limit for next recursion
	if n ==0:return answer # if end return answer
	else:return find_perm(new_limit,working_copy,answer) # else continue recursion


print(find_perm(999999))# answer
print(find_perm(3628799))#last possible permutation