#_______Description_____

#https://projecteuler.net/problem=19
#You are given the following information, but you may prefer to do some research for yourself.
#1 Jan 1900 was a Monday.
#Thirty days has September,
#April, June and November.
#All the rest have thirty-one,
#Saving February alone,
#Which has twenty-eight, rain or shine.
#And on leap years, twenty-nine.
#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
##_______end_description_____:

#loop in a loop in a loop :)
day=0
count=0

for y in range(1900,2001):# loop years
    for m in range (1,13):# loop months
        if m==2:# if feb
            if y %4==0: #if leap
                c=29
                if y%100==0 and y%400!=0: #make sure if leap
                    c=28
            else:
                c=28
        elif m==4 or m==6 or m==9 or m==11: #if month with 30
            c=30
        else:
            c=31
        for d in range(1,c+1): # loop days
            if y>=1901:   #start 1901 as per instructions
                if day==6 and d==1: # if sunday and first of month
                    count+=1 
            if day==6: # if sunday- restart day to 0
                day=0
            else: #add to day of the week
                day+=1

print(count)