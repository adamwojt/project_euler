#_______Description_____

#https://projecteuler.net/problem=36
#The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#(Please note that the palindromic number, in either base, may not include leading zeros.)
##_______end_description_____:
from eulertools import is_palindrome #importing, same as in euler4.py
def to_binary(n): #translate to binary
    number=bin(n)
    return number[2:]

answer=sum([i for i in range(1,10**6) if all((is_palindrome(str(i)),is_palindrome(to_binary(i))))]) #summing all that meet condition
print(answer)