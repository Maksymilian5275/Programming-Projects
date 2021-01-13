'''
Lattice Paths
How many routes are there through a 20×20 grid?
'''

import math
import time as t

def latticenum(n):
    return (math.factorial(2*n))/(math.factorial(n)*math.factorial(n))

start_time = t.time()

print("The number of routes through a 20x20 grid where you can only go right and down is",int(latticenum(20)),
"\nThis code took",t.time()-start_time,"seconds to run")