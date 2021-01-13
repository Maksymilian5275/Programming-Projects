'''
Counting Sundays
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

import time as t

Day28=[2]
Day30=[4,6,9,11]
Day31=[1,3,5,7,8,10,12]
suncount=0
day=1

start_time = t.time()

for i in range(1900,2001):
    for j in range(1,13):
        if i%400==0 and j in Day28:
            day=(day+29)%7
        elif i%100!=0 and i%4==0 and j in Day28:
            day=(day+29)%7
        elif i%4!=0 and j in Day28:
            day=(day+28)%7
        elif j in Day30:
            day=(day+30)%7
        elif j in Day31:
            day=(day+31)%7
        if day%7==0 and i > 1900:
            suncount+=1

print("The number of Sundays that fell on the first of the month during the 20th century is",suncount,
"\nThis code took",t.time()-start_time,"seconds to run")