# _______Description_____

# https://projecteuler.net/problem=57
# It is possible to show that the square root of two can be expressed as an infinite continued fraction.
# $\sqrt 2 =1+ \frac 1 {2+ \frac 1 {2 +\frac 1 {2+ \dots}}}$
# By expanding this for the first four iterations, we get:
# $1 + \frac 1 2 = \frac  32 = 1.5$
# $1 + \frac 1 {2 + \frac 1 2} = \frac 7 5 = 1.4$
# $1 + \frac 1 {2 + \frac 1 {2+\frac 1 2}} = \frac {17}{12} = 1.41666 \dots$
# $1 + \frac 1 {2 + \frac 1 {2+\frac 1 {2+\frac 1 2}}} = \frac {41}{29} = 1.41379 \dots$
# The next three expansions are $\frac {99}{70}$, $\frac {239}{169}$, and $\frac {577}{408}$, but the eighth expansion, $\frac {1393}{985}$, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.
# In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?
# #_______end_description_____:


from fractions import Fraction
import math


def generate_sqrt_two(n):
    start = Fraction(1, 2)
    for _ in range(n):
        full = 1 + start
        start = 1 / (2 + start)
        yield full


def num_of_digits(n):
    return int(math.log10(n)) + 1


def main(expansions):
    res = 0
    dig = num_of_digits
    for exp in generate_sqrt_two(expansions):
        if dig(exp.numerator) > dig(exp.denominator):
            res += 1
    return res


if __name__ == '__main__':
    result = main(1000)
    print(result)
