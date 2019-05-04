#_______Description_____

#https://projecteuler.net/problem=26
#A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
#
#1/2= 0.5
#1/3= 0.(3)
#1/4= 0.25
#1/5= 0.2
#1/6= 0.1(6)
#1/7= 0.(142857)
#1/8= 0.125
#1/9= 0.(1)
#1/10= 0.1
#
#Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
#Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
##_______end_description_____:

def decimals(number):
    dividend = 1;remainder = 1
    remainderlist=[];remainder_set=set()
    while remainder:
        remainder = dividend % number # calculate remainder
        if remainder in remainder_set: #check if it's already in set (using sets membership check for performance)
            return len(remainderlist[remainderlist.index(remainder):]) #return lenght of reccuring cycle
        if remainder < number: #if smaller - get another decimal
            dividend = remainder * 10
        else:
            dividend = remainder
        remainderlist.append(remainder) #add to list
        remainder_set.add(remainder)#add to set
  
score=max(filter(None,(decimals(x) for x in range(1,1000)))) #check highest
print(score)