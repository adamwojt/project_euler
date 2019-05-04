#_______Description_____

#https://projecteuler.net/problem=9
#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.Find the product abc.
##_______end_description_____:
exitFlag = False

for n in range(1,500):
    for m in range(n,500):
        c=m**2+n**2
        a=m**2-n**2
        b=2*m*n
        if a+b+c==1000:
            print(a*b*c,a,b,c)
            exitFlag = True
    if exitFlag:
        break

