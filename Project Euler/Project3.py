'''
Largest Prime Factor
What is the largest prime factor of the number 600851475143
'''

import math
import time as t

N=600851475143
bound=round(math.sqrt(N))+1
primes=[]
factors=[]
factor=2

start_time = t.time()

while factor<(bound):
    if N%factor==0:
        factors.append(factor)
        factor+=1
    else:
        factor+=1

k=2
for i in factors:
    while k<i:
        if i%k==0:
            break
        elif i%k!=0:
            k+=1
            continue
    if k==i:
        primes.append(i)
    k=2
        
print("The largest prime factor of",N,"is",max(primes),
"\nThis code took",t.time()-start_time,"second to run")