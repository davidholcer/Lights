#!/usr/bin/env python3

from light import *

colorss=["#9400D3","#4B0082","#0000FF","#00FF00","#FFFF00","#FF7F00","#FF0000"]
def rainbow(colorss,many=3,cycles=0,DELAY=0.3):
    pos=0
    times=0
    if (cycles==0):cycles=100000
    inc=1
    while times<2*cycles:
        setColor(colorss[pos],bstick,start=14,end=32)
        prev=copy.copy(pos)
        pos+=inc
        if pos%(len(colorss)-1)==0:
            times+=1
            inc*=-1
        time.sleep(DELAY)
        #print((prev,pos))
        between=(inBetween(colorss[prev],colorss[pos],many=10))
        c=1
        while c<len(between)-1:
            #print(between[c])
            setColor(between[c],bstick,start=14,end=32)
            time.sleep(DELAY)
            c+=1
        setColor(colorss[pos],bstick,start=14,end=32)

rainbow(colorss,DELAY=0.5)
