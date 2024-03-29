#Some common functions used throughout the project.

def Sieve(n): #returns list of primes up to limit- n
    out = []
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if (sieve[p]):
            out.append(p)
            for i in range(p, n+1, p):
                sieve[i] = False
    return out

def cyclic_perm(n): #returns list of cyclic permutations
    perms=[n[i:]+n[:i] for i in range(len(n))]
    return perms

def is_palindrome(s): #returns True if string is palindrome
    if s== '':
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False

def to_binary(n): #converts number to binary
    number=bin(n)
    return number[2:]

def is_pandigital(n): #returns True if n is pandigital. ex. 3214 will give True
    lenght=len(str(n))
    digits=['1','2','3','4','5','6','7','8','9','0']
    if all(i in str(n) for i in set(digits[0:lenght])):
        return True
    else:
        return False
    
def most_common(lst): #returns most common element in the list
    return max(set(lst), key=lst.count)

def _try_composite(a, d, n, s): #part of is_prime method
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite
 

#below was taken from 'https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test'. I did wrote my own primarity test functions throughout the project, this one was used when performance was needed for large n.


def is_prime(n, _precision_for_huge_n=16): #returns True for primes; good performance for large primes but not small.
    if n in _known_primes:
        return True
    if any((n % p) == 0 for p in _known_primes) or n in (0, 1):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    if n < 1373653: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467: 
        if n == 3215031751: 
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s) 
                   for a in _known_primes[:_precision_for_huge_n])
 
_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]
