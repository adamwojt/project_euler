#_______Description_____

#https://projecteuler.net/problem=6
#The sum of the squares of the first ten natural numbers is,
#12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
##_______end_description_____:
def find_difference(LowerLimit,HigherLimit):
    AllNumbers=[]
    for x in range(LowerLimit,HigherLimit):
        AllNumbers.append(x)
    AllSqrd=[]
    for n in AllNumbers:
        n2=n**2
        AllSqrd.append(n2)
    Difference= (sum(AllNumbers))**2-(sum(AllSqrd))
         
    return Difference
print(find_difference(1,101))
#     
print(sum(range(101))**2 - sum(i*i for i in range(101)))