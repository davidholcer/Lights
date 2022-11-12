#!/usr/bin/env python3

from light import *
import sys 
startLight=int(sys.argv[1])

colorss=["#9400D3","#4B0082","#0000FF","#00FF00","#FFFF00","#FF7F00","#FF0000"]
def rainbow(colorss,many=3,cycles=100000,DELAY=0.005):
    pos=0
    times=0
    inc=1
    while times<2*cycles:
        setColor(colorss[pos],bstick,startLight,32)
        prev=copy.copy(pos)
        pos+=inc
        if pos%(len(colorss)-1)==0:
            times+=1
            inc*=-1
        time.sleep(DELAY)
        #print((prev,pos))
        between=(inBetween(colorss[prev],colorss[pos],many=20))
        c=1
        while c<len(between)-1:
            #print(between[c])
            setColor(between[c],bstick,startLight,32)
            time.sleep(DELAY)
            c+=1
        setColor(colorss[pos],bstick,startLight,end=32)

rainbow(colorss,DELAY=0.5)
# multiRainbow(colorss,DELAY=0.5)