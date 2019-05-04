#_______Description_____

#https://projecteuler.net/problem=28
#Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#21 22 23 24 25
#20  7  8  9 10
#19  6  1  2 11
#18  5  4  3 1217 16 15 14 13
#It can be verified that the sum of the numbers on the diagonals is 101.
#What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
##_______end_description_____:


count=1;last=1
for n in range(3,1002,2): #loop through spiral
        for i in range(last,(n**2)+1,n-1): #increase size with quadratic function
            if i==last:pass # skip first term- it's the same as previous loop's last one
            else:count+=i #add to count
            last=i #set last term
print(count)
