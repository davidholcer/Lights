#!/usr/bin/env python3

from distutils.log import debug
from light import *
import sys 
startLight=int(sys.argv[1])
verbose=True if "-v" in sys.argv else False

#setColor("#ff0",bstick,start=14,end=32)
intv=1

#print(int(time.time() - startTime))

DELAY=0.001

colors=[0]*5

inc=1
i=0
first=True

#while (int((time.time() - startTime))<900):
while True:
    #if (int((time.time() - startTime)*1000)%(intv*1000)==0):
    if first:
        c1=screenColorGrabber(save=False,NUM_CLUSTERS = 5,rgb=False,DEBUG=False)
        colors[i]=c1
        colors[i+1]=c1
        

    if first==False:
        ib=inBetween(colors[i],colors[(i+1)%len(colors)])
        j=0
        while j<len(ib):
            setColor(ib[j],bstick,startLight,32)
            time.sleep(DELAY)
            j+=1

        i=(i+1)%(len(colors))
    first=False

    # time.sleep(0.5)
    c2=screenColorGrabber(save=False,NUM_CLUSTERS = 5,rgb=False,DEBUG=False)
    colors[(i+1)%len(colors)]=c2
    
    if verbose: print(colors,"COLORS")

    time.sleep(DELAY)
    
# ['#204C44' '#5F406D' '#5F5852' '#494440' '#312E2C' '#373331' '#3B3735'] O