#_______Description_____

#https://projecteuler.net/problem=22
#Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
#For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
#What is the total of all the name scores in the file?
##_______end_description_____:
from string import ascii_uppercase
 
namestxt =open('names.txt', 'r') #open file
namesli=sorted([i.replace('"','') for i in namestxt.read().split(',')]) #make list of names
score={};start=1
for c in ascii_uppercase: # make dict of letter scores, later i found that ord(letter)+64 does the same
    score[c]=start
    start+=1

def scores(name): #name score fuction
        letterscore=0
        for i in str(name): #calculate letterscore
            letterscore+=score[i]
        return letterscore*(namesli.index(name)+1) #add position
 
 
print(sum(scores(n) for n in namesli)) #print result
