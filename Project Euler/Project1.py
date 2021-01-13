'''
Multiples of 3 and 5:
Find the sum of all the multiples of 3 or 5 below 1000.
'''
import time as t

count=0

start_time = t.time()

for i in range(0,1000):
    if i%3==0:
        count+=i
    elif i%5==0:
        count+=i
    
print("The sum of all the multiples of 3 and 5 below 1000 is equal to",count,
"\nThis program took",t.time()-start_time,"seconds to run")