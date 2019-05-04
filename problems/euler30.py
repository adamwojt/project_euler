#_______Description_____

#https://projecteuler.net/problem=30
#Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#1634 = 14 + 64 + 34 + 44
#8208 = 84 + 24 + 04 + 84
#9474 = 94 + 44 + 74 + 44
#As 1 = 14 is not a sum it is not included.
#The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
##_______end_description_____:
#original


#original loop i did didn't use dictionary for finding sums for sets of digits and performed 2x slower.

scores=[] #list of valid numbers
dict_power={} #dict for storing sets of sums for sets of digits.
for i in range(10,354294): # safe limit as 6*(9^5)
    strg=str(i)
    set_str=frozenset(strg)
    getter= dict_power.get(set_str)
    if getter: # check if None (helps performance) 
        if getter== i: #check if fits
            scores.append(i) #appends score
    else:
        sumstrg=sum(int(x)**5 for x in strg) #calculate power
        dict_power[set_str]=sumstrg #add sum to dictionary
        if sumstrg==i:# check if fits
            scores.append(i) #append score

print(sum(scores))
print(scores)

