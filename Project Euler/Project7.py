'''
10001st prime
Find the 10001st prime.
'''

import math
import time as t

primecount=1
count=0
prime=0
n=10001
bound=round(n*(math.log(n)+math.log(math.log(n)))+1)
seq=list(range(3,bound+1,2))
primes=[2,3,5,7,11]

start_time = t.time()

for k in primes:
    for j in seq:
        if j%k==0 and j!=k:
            seq.remove(j)
        else:
            continue

for j in seq:
    for k in primes:
        if j%k!=0:
            count+=1
            if count==len(primes):
                primes.append(j)
    count=0

print("The 10001st prime number is",primes[10000],
"\nThis code took",t.time()-start_time,"seconds to run")