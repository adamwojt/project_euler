#_______Description_____

#https://projecteuler.net/problem=52
#It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
#Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
##_______end_description_____:
print(next(i for i in range(1,10**6) if all([set(str(i))==set(str(i*n)) for n in range(2,7)])))