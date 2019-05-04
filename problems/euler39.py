#_______Description_____

#https://projecteuler.net/problem=39
#If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
#{20,48,52}, {24,45,51}, {30,40,50}
#For which value of p ≤ 1000, is the number of solutions maximised?
##_______end_description_____:

def most_common(lst): # return most common element in list
	return max(lst, key=lst.count)

allp=[]
for n in range(1,1000):  #see https://en.wikipedia.org/wiki/Formulas_for_generating_Pythagorean_triples
    for m in range(n,1000):
        c=((m**2)+(n**2))/2
        a=m*n
        b=((m**2)-(n**2))/2
        p=int(a+b+c)
        if p>1000:
            break
        allp.append(p)

print(most_common(allp))
