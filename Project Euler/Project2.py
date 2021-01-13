'''
Even Fibonacci Numbers
By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even-valued terms.
'''

import time as t

F2=1
F3=2
temp=0
fibcount=0

start_time = t.time()

while F3<4000000:
    if F3%2==0:
        fibcount+=F3
    temp=F3+F2
    F2=F3
    F3=temp

print("The sum of all even Fibonacci numbers below 4 million is",fibcount,
"\nThis program took",t.time()-start_time,"seconds to run")