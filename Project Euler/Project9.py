'''
Special Pythagorean Triplet
There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
'''

import time as t

cond=False
i=0

start_time = t.time()

while cond==False and i<500:
    i+=1
    for j in range(1,500):
        for k in range(1,500):
            if (i**2)+(j**2)==(k**2) and i+j+k==1000:
                produ=i*j*k
                a,b,c=i,j,k
                cond=True

print("The Pythagorean triplet for which a + b + c = 1000 is a=",a,", b=",b,", c=",c," and abc=",produ,
"\nThis code took",t.time()-start_time,"to run")