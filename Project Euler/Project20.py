'''
Factorial Digit Sum
Find the sum of the digits in the number (100!)
'''

import math
import time as t

res=str(math.factorial(100))
digsum=0

start_time = t.time()

for i in range(0,len(res)):
    digsum+=int(res[i])
    
print("The sum of the digits in 100! is",digsum,
"\nThis code took",t.time()-start_time,"seconds to run")