#_______Description_____

#https://projecteuler.net/problem=34
#145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#Note: as 1! = 1 and 2! = 2 are not sums they are not included.
##_______end_description_____:

from math import factorial

answers=set()

for i in range(10,100000):# range guessed ;)
    x=0
    for n in str(i):
        x+=factorial(int(n))
    if x==i:
        answers.add(i)
print(sum(answers))
