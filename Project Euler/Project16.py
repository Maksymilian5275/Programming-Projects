'''
Power Digit Sum
What is the sum of the digits of the number 2^(1000)?
'''

import time as t


total=0

start_time = t.time()

N=str(2**1000)
for i in range(0,len(N)):
    total+=int(N[i])

print("The sum of the digits in the number 2^(1000) is",total,
"\nThis code took",t.time()-start_time,"seconds to run")