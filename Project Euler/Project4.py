'''
Largest Palindrome Product
Find the largest palindrome made from the product of two 3-digit numbers.
'''

import time as t

palcheck=0
temp=0
maxp=0

start_time = t.time()
for i in range(1000,100,-1):
    for j in range(1000,100,-1):
        temp=str(i*j)
        palcheck=temp[::-1]
        if temp==palcheck and int(palcheck)>maxp:
            maxp=int(palcheck)
            break

print("The largest palindrome made by the product of two 3-digit numbers is",maxp,
"\nThis code took",t.time()-start_time,"seconds to run")