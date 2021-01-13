'''
Smallest Multiple
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

import math
import time as t

i=20
count=0
temp=0
factorlist=[]
primes=[2,3,5,7,11,13,17,19]

start_time = t.time()
for k in primes:
    for j in range(2,21):
        if math.log(j,k)%1==0 or math.log(j,k)%2==0 or math.log(j,k)%3==0 or math.log(j,k)%4==0:
            temp=math.log(j,k)
        if j ==20:
            for l in range(0,int(temp)):
                factorlist.append(k)
    temp=0    
total=1
for g in factorlist:
    total*=g

print("The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is",total,
"\nThis code took",t.time()-start_time,"seconds to run")