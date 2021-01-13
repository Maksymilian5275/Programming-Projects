'''
Sum square difference
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

import time as t

sqofsum=0
sumofsq=0

start_time = t.time()
for i in range(1,101):
    sumofsq+=(i**2)
    sqofsum+=i

print("The difference between the sum of the squares of the first one hundred natural numbers",
"and the square of the sum is",(sqofsum**2)-sumofsq,
"\nThis code took",t.time()-start_time,"seconds to run")