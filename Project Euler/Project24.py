'''
Lexicographic Permutations
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

import math
import time as t

def lex(x, num):
    
    for p in range(math.factorial(len(x))):
        if p==num-1:
            res = ''.join(x)
            return res
        
        i=len(x)-1
        while i>0 and x[i-1]>x[i]:
            i-=1

        x[i:]=reversed(x[i:])
        if i>0:
            q=i
            while x[i-1]>x[q]:
                q+=1
                
            temp=x[i-1]
            x[i-1]=x[q]
            x[q]=temp

s='0123456789'
s=list(s)
num=1000000

start_time = t.time()

res=lex(s, num)
print("Lexographic permutation number",num,"of the numbers between 0 and 9 is",res,
"\nThis code took",t.time()-start_time,"seconds to run")
