'''
Name Scores
What is the total of all the name scores in the file?
'''

import time as t

f=open("PEuler22.txt", "r")
f1=f.read()
f1=f1.strip()
f1=f1.replace("\"","").split(",")

def namescore(x):
    score=0
    alpha="abcdefghijklmnopqrstuvwxyz"
    imie=x.lower()
    for i in range(0,len(imie)):
        for j in range(0,len(alpha)):
            if imie[i]==alpha[j]:
                score+=(j+1)
            else:
                continue
    return score

total=0

start_time =t.time()

names=sorted(f1)
for k in range(0,len(names)):
    temp=namescore(names[k])
    total+=(temp*(k+1))
    
print("The total of all the namescores in the file is ",total,
"\nThis code took",t.time()-start_time,"seconds to run")