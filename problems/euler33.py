#_______Description_____

#https://projecteuler.net/problem=33
#The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
#If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
##_______end_description_____:
pairsc=[]
for d in range(11,99): #create pairs with same digits
    for n in range(10,d):
        x=(str(n),str(d))
        for n in x[1]:
            if n in x[0]:
                pairsc.append(x)

pairsbadmath=[]
for i in pairsc: #do 'bad maths' reduction
    io='';it=''
    for n in i[1]:
        if n in i[0]:
            io=i[0].replace(str(n),'',1)
            it=i[1].replace(str(n),'',1)
    pairsbadmath.append((io,it))

answer=[];count=0
for i in pairsbadmath: #check if ratios are the same for same pairs
    if int(i[1])==0:
        pass
    else:
        ratiobad=int(i[0])/int(i[1])
        ratiogood=int(pairsc[count][0])/int(pairsc[count][1])
        if ratiobad==ratiogood and int(pairsc[count][1][1])!=0:
            answer.append(pairsc[count])
    count+=1

def gcd(a, b): #find common denominator
    while b:
        a, b = b, a % b
    return a

print(answer)
n=1;d=1
for i in range(len(answer)): #multiply , get numerator and denominator
    n*=int(answer[i][0])
    d*=int(answer[i][1])

print(d/gcd(n,d))# print answer
