#_______Description_____
#https://projecteuler.net/problem=18
#By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
#37 4
#2 4 6
#8 5 9 3
#That is, 3 + 7 + 4 + 9 = 23.
#Find the maximum total from top to bottom of the triangle below:
#75
#95 64
#17 47 82
#18 35 87 10
#20 04 82 47 65
#19 01 23 75 03 34
#88 02 77 73 07 63 67
#99 65 04 28 06 16 70 92
#41 41 26 56 83 40 80 70 33
#41 48 72 33 47 32 37 16 94 29
#53 71 44 65 25 43 91 52 97 51 14
#70 11 33 28 77 73 17 78 39 68 17 57
#91 71 52 38 17 14 91 43 58 50 27 29 48
#63 66 04 68 89 53 67 30 73 16 69 87 40 31
#04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
#NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
##_______end_description_____:

copypaste='''75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

a=0;b=2;triangle=[]
while b<=len(copypaste): #loop to list all numbers from the string
    triangle.append(int(copypaste[a:b]));a+=3;b+=3    
    
#Below loop navigates through list of numbers- translating it to 2d triangle 
#How method works: we are looking at for ex 63 in second last row. We are choosing biggest of 
#two possible steps(04,62), then we add 62 to 63 above and continue this process until top of triangle;
#which then reduces it to one maximum answer.

for i in range (13,-1,-1): # loop bottom to up through triangle's layers starting second last
    for t in range (0,i+1): #loop through layer's numbers
        positionrow1=int(((i*(i+1))/2)+t) #calculate position of current's layer step 
        positionrow2=int((((i+1)*(i+2))/2)+t)# calculate position of below's step
        maxtip=max((triangle[positionrow2]),(triangle[positionrow2+1])) #check max score for two possible options
        triangle[positionrow1]+=maxtip # add highest possible option to the top one

print(triangle[0])
