#_______Description_____

#https://projecteuler.net/problem=67
#By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
#37 4
#2 4 6
#8 5 9 3
#That is, 3 + 7 + 4 + 9 = 23.
#Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.
#NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
##_______end_description_____:
triangletxt =open('triangle.txt', 'r')
triangleread=str(triangletxt.read())
a=0
b=2
triangle=[]
while b<=len(triangleread):
    triangle.append(int(triangleread[a:b]))
    a+=3
    b+=3
  
for i in range (98,-1,-1):
    for t in range (0,i+1):
        positionrow1=int(((i*(i+1))/2)+t)
        positionrow2=int((((i+1)*(i+2))/2)+t)
        maxtip=max((triangle[positionrow2]),(triangle[positionrow2+1]))
        triangle[positionrow1]+=maxtip
   
print(triangle[0])

