'''
Summation of Primes
Find the sum of all the primes below two million.
'''

import time as t

prinums=set(range(3, 2000000+1,2))

start_time = t.time()

for k in range(3,int(2000000**(0.5)+1)):
    if k not in prinums:
        continue
    num=k
    while num<2000000:
        num+=k
        if num in prinums:
            prinums.remove(num)
print("The sum of all the prime numbers below 2,000,000 is",2+sum(prinums),
"\nThis code took",t.time()-start_time,"seconds to run")