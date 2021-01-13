'''
Non-Abundant Sums
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

import math
import time as t

def divisors(x):
    if (x==1):
        return 1
    
    n=math.ceil(math.sqrt(x))
    total=1
    divisor=2
    
    while(divisor<n):
        if(x%divisor==0):
            total+=divisor
            total+=x//divisor
        divisor+=1
    if (n**2==x):
        total+=n
    return total

def abund(x):
    if (divisors(x)>x):
        return True
    else:
        return False

abundlist=[] 

start_time=t.time()

for x in range(0,28124):
    if (abund(x)):
        abundlist.append(x)
del abundlist[0]

sums=[0]*28124
for x in range(0,len(abundlist)):
    for y in range(x, len(abundlist)):
        sumab=abundlist[x]+abundlist[y]
        if sumab<28124:
            if sums[sumab]==0:
                sums[sumab]=sumab

ans=0
for i in range(0, len(sums)):
    if sums[i]==0:
        ans+=i
print("The sum of all the positive integers which cannot be written as the sum of two abundant numbers is",ans,
"\nThis code took",t.time()-start_time,"seconds to run")