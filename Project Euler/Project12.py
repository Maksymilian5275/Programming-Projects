'''
Highly Divisible Triangular Number
What is the value of the first triangle number to have over five hundred divisors?
'''

import math
import time as t

def divisors(n):
    num=0
    for i in range(1, int(math.sqrt(n))+1):
        if n%i==0:
            num+=2
        if i*i==n:
            num-=1
    return num

count=0

start_time = t.time()

for n in range(1, 20000):
    Tn=n*(n+1)/2
    if n%2==0:
        count=divisors(n/2)*divisors(n+1)
    else:
        count=divisors(n)*divisors((n+1)/2)
    if count>500:
        ans = int(Tn)
        break

print("The first triangle number to have over 500 divisors is",ans,
"\nThis code took",t.time()-start_time,"seconds to run")