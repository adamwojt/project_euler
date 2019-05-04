#_______Description_____

#https://projecteuler.net/problem=31
#In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
#It is possible to make £2 in the following way:
#1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
#How many different ways can £2 be made using any number of coins?
##_______end_description_____:
#In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
#It is possible to make £2 in the following way:
#1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
#How many different ways can £2 be made using any number of coins?

final = 200  # total sum
nominals = [1, 2,5, 10, 20, 50, 100, 200] #list of nominals
ways = [1] + [0]*final  #create list with 200 positions, 1 for 1 way to write 1 p

for nominal in nominals: #loop nominals
    for i in range(nominal, final+1): #1p loop will be 1-200, for 2p, 2-200 etc.
    	ways[i] += ways[i-nominal] # after 1p loop we will have 1s everyone in list. after 2p we will have 1,2,2,3,3,4,4,5,5 etc.

print(ways[-1]) #print last position

