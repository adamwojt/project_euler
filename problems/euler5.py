#_______Description_____

#https://projecteuler.net/problem=5
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
##_______end_description_____:
# #FIRST SOLUTION- CHEECKY
# import time
# t = time.time()
# for i in range(0,100000000000000,2520):
#         if i%11==0:
#             if i%13==0:
#                 if i%16==0:
#                     if i%17==0:
#                         if i%19==0 and i!=0:
#                             print(i)
#                             break
# timer=time.time()-t
# print(timer,"sec")
#  
# t = time.time()
#  
#  
#  
# #SECOND SOLUTION- LESS CHEECKY
#  for i in range(0,100000000000000,2520):
#      n=11
#      while n<=20:
#          if i%n==0:
#              n+=1
#              if n==20 and i!=0:
#                  print(i)
#                  break
#          else:
#              break
#      if n==20 and i!=0:
#          break
#      
# timer=time.time()-t
#  print(timer,"sec")




    
            
             
            
    