'''
Number Letter Counts
If all the numbers from 1 to 1000 inclusive were written out in words, how many letters would be used?
'''

import time as t


def numletcount(t):
    n=str(t)
    cnt=0
    while len(n)>0:
        if n == "0":
            n=""
            
        if len(n)==1:
            if n == "1" or n == "2" or n == "6":
                cnt+=3
                n=""
            if n == "4" or n == "5" or n == "9":
                cnt+=4
                n=""
            if n == "3" or n == "7" or n == "8":
                cnt+=5
                n=""
                
        if len(n)==2:
            if n[0]=="0":
                n=n[1]
            elif n[1]=="0":
                if n[0]=="1":
                    cnt+=3
                    n=""
                elif n[0] == "2" or n[0] == "3" or n[0] == "8" or n[0] == "9":
                    cnt+=6
                    n=""
                elif n[0] == "4" or n[0] == "5" or n[0] == "6":
                    cnt+=5
                    n=""
                elif n[-2] == "7":
                    cnt+=7
                    n=""
            else:
                if n[0]=="1":
                    if n[-1] == "1" or n[-1] == "2":
                        cnt+=6
                        n=""
                    elif n[-1] == "5" or n[-1] == "6":
                        cnt+=7
                        n=""
                    elif n[-1] == "3" or n[-1] == "4" or n[-1] == "8" or n[-1] == "9":
                        cnt+=8
                        n=""
                    elif n[-1] == "7":
                        cnt+=9
                        n=""
                elif n[0] == "2" or n[0] == "3" or n[0] == "8" or n[0] == "9":
                    cnt+=6
                    n=n[-1]
                elif n[0] == "4" or n[0] == "5" or n[0] == "6":
                    cnt+=5
                    n=n[-1]
                elif n[0] == "7":
                    cnt+=7
                    n=n[-1]
            
        if len(n)==3:
            if n[1:3] == "00":
                cnt+=7
                n=n[0]
            else:
                if n[0] == "1" or n[0] == "2" or n[0] == "6":
                    cnt+=13
                    n=n[1:3]
                elif n[0] == "4" or n[0] == "5" or n[0] == "9":
                    cnt+=14
                    n=n[1:3]
                elif n[0] == "3" or n[0] == "7" or n[0] == "8":
                    cnt+=15
                    n=n[1:3]
        if len(n)==4:
            cnt+=11
            n=""
    return cnt

nlctot=0

start_time = t.time()

for i in range(1,1001):
    nlctot+=numletcount(i)

print("The number of letters used in all the numbers (in words) from 1 to 1000 is",nlctot,
"\nThis code took",t.time()-start_time,"seconds to run")