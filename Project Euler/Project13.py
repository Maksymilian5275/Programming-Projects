'''
Large Sum
Work out the first ten digits of the sum of the one-hundred 50-digit numbers in "PEuler13.txt".
'''

import time as t

f = open("PEuler13.txt", "r")
total=0

start_time = t.time()

for l in f:
    total+=int(l)

print("The first ten digits of the sum of the one-hundred numbers is",str(total)[0:10:],
"\nThis code took",t.time()-start_time,"seconds to run")