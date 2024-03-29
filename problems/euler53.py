#_______Description_____

#https://projecteuler.net/problem=53
#There are exactly ten ways of selecting three from five, 12345:
#123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
#In combinatorics, we use the notation, $^{5}C_{3} = 10$.
#In general, $^{n}C_{r} = \dfrac{n!}{r!(n-r)!}$, where $r \le n$, $n! = n \times (n-1) \times ... \times 3 \times 2 \times 1$, and $0! = 1$.
#
#It is not until $n = 23$, that a value exceeds one-million: $^{23}C_{10} = 1144066$.
#How many, not necessarily distinct, values of $^{n}C_{r}$ for $1 \le n \le 100$, are greater than one-million?
##_______end_description_____:
ways=0
from math import factorial as f
for n in range(1,101):
    for r in range(1,n+1):
        if f(n)/(f(r)*f(n-r)) >10**6:
            ways+=1
print(ways)