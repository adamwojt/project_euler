#_______Description_____

#https://projecteuler.net/problem=38
#Take the number 192 and multiply it by each of 1, 2, and 3:
#192 × 1 = 192
#192 × 2 = 384
#192 × 3 = 576
#By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
#The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
#What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
##_______end_description_____:
def is_pandigital(n):  #check if pandigital using list of digits
    lenght=len(str(n))
    if lenght !=9:
        return False
    digits=['1','2','3','4','5','6','7','8','9']
    if all(i in str(n) for i in digits[0:lenght]):
        return True
    else:
        return False

def find_m(n): #function keeps multiplying  by 1,2,3 etc. until product is 9 digits long
    product=''
    m=0
    while len(product)<=8:
        m+=1
        product+=str(n*m)
        
    if is_pandigital(product):
        return int(product) 
    else:
        return False

maxx=0;n=0
for i in range(1,10000):# reasonable limit
    temp_=find_m(i) 
    if temp_: #update the score, last biggest i if find_m(i) wins:
        maxx=temp_
        n=i
print(n)
