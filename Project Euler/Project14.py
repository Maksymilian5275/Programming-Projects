'''
Longest Collatz Sequence
Which starting number, under one million, produces the longest chain?
'''

import time as t

def collatz(n):
    ctr = 0
    while n > 1:
        if n % 2 == 0:
            n = n/2
            ctr+=1
        else:
            n = 3*n +1
            ctr+=1
    return ctr

collatzmax=0

start_time = t.time()

for i in range(1,1000001):
    tempcol=collatz(i)
    if tempcol>collatzmax:
        collatzmax=tempcol
        startmax=i
    
print("The starting number under 1,000,000 which produces the longest sequence is",startmax,
"\nThis code took",t.time()-start_time,"seconds to run")