'''
1000-Digit Fibonacci Number
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''

import time as t

def fibo(lim):
    i=2
    temp=0
    f_n=1
    f_n1=1
    while len(str(temp))<lim:
        
        temp=f_n+f_n1
        f_n=f_n1
        f_n1=temp
        
        i+=1
    
    return [i, f_n1]

start_time=t.time()

i,fn1=fibo(1000)

print("The index of the first 1000 digit Fibonacci number is",i,
"\nThis code took",t.time()-start_time,"seconds to run")    