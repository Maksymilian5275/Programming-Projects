'''
Amicable Numbers
Evaluate the sum of all the amicable numbers under 10000.
'''
import math
import time as t

def amcalc(x):
    divlist_a=[1]
    divlist_b=[1]
    a=x
    
    if x==1:
        return "Fail"
    
    elif x!=1:
        
        for i in range(2,int(math.sqrt(a)+1)):
            if a%i==0:
                divlist_a.extend((i, int(a/i)))      
        b=int(sum(divlist_a))
        for i in range(2,int(math.sqrt(b)+1)):
            if b%i==0:
                divlist_b.extend((i, b/i))
        c=int(sum(divlist_b))
        
    if c==a and a!=b:
        return a,b
    else:
        return "Fail"

amnums=[]
numlist=list(range(1,10001))

start_time = t.time()

for k in numlist:
    ams=amcalc(k)
    if ams=="Fail":
        continue
    else:
        #ams=list(ams)
        numlist.remove(ams[0])
        numlist.remove(ams[1])
        amnums.extend((ams))
    
print("The sum of all the amicable numbers under 10,000 is",sum(amnums),
"\nThis code took",t.time()-start_time,"seconds to run")