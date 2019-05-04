#_______Description_____

#https://projecteuler.net/problem=16
#215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 21000?
##_______end_description_____:
names={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',1000:'onethousand'}
allnames=''
 
def join_10s(n):
    try:
        return names[n]
    except:
        t=int(str(n)[0:1])*10
        r=n-int(str(n)[0:1])*10
        return names[t]+names[r]
 
def join_100s(n): 
    try:
        h=int(str(n)[0:1])
        tr=join_10s(n-h*100)
        return names[h]+'hundred'+'and'+tr
    except:
        return names[h]+"hundred"
     
for n in range (1,1001):
    try:
        name=names[n]
        allnames+=name
    except:
        if n<100:
            name=join_10s(n)
            allnames+=name
        else:
            name=join_100s(n)
            allnames+=name
             
