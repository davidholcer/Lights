#!/usr/bin/env python3

from light import *
import sys

verbose=True if "-v" in sys.argv else False
# startLight=int(sys.argv[1])
# startColor=int(sys.argv[2])
# endColor=int(sys.argv[3])

startLight=0
startColor="#9400D3"
endColor="#00FF00"

colorss=["#9400D3","#4B0082","#0000FF","#00FF00","#FFFF00","#FF7F00","#FF0000"]
# colorss=["#0000FF","#FF0000"]


def gradient(sC,eC,sL=0,eL=32,incF=1,rev=False,cDELAY=0.01):
    # setColor(colorss[pos],bstick,startLight,32)
    first=True
    inc=-1 if (rev==True) else 1

    while True:
        cols=inBetween(sC,eC,abs(eL-sL)) if first else inBetween(cols[1],eC,abs(eL-sL))
        first=False
        DELAY = 0.001
        for i in range(sL, eL//incF,1):
            l=eL-1-i*incF if (rev==True) else i*incF
            try:bstick.set_color(channel=0, index=l, hex=cols[i*incF])
            except:pass
            time.sleep(DELAY)

        time.sleep(cDELAY)

# gradient(startColor,endColor,incF=1,rev=True)

def continuousRainbow(switchTimes,sL=0,eL=32,incF=1,rev=False,cDELAY=0.01):
    first=True
    inc=-1 if (rev==True) else 1
    #rainbow color index
    rci=2
    times=0

    while True:
        if first:
            cols=inBetween(colorss[0],colorss[1],abs(eL-sL))
            times+=1
        else:
            if verbose: print(times)
            
            ith=len(colorss)-1-abs(len(colorss)-1-rci%(2*( len(colorss)-1 ) )) 
            if verbose: print(ith,"I")
            # rev=(not rev) if (ith%(len(colorss)-1)==0) else rev
            if verbose: print (rev,"R")
            if times==switchTimes:
                rci+=1
                if (ith%(len(colorss)-1)==0): rev=(not rev)
                times=0
                time.sleep(1)
                #bounce back
            nextInBetween=inBetween(cols[-1],colorss[ith ],abs(eL-sL))
            # print(nextInBetween)
            # cols=inBetween(cols[1],colorss[rci%len(colorss)],abs(eL-sL))
            cols=inBetween(cols[2],nextInBetween[len(nextInBetween)//12],abs(eL-sL))
            times+=1
# 16,6, 15
        first=False
        DELAY = 0.001
        for i in range(sL, eL//incF,1):
            l=eL-1-i*incF if (rev==True) else i*incF
            try:bstick.set_color(channel=0, index=l, hex=cols[i*incF])
            except:pass
            time.sleep(DELAY)

        time.sleep(cDELAY)

continuousRainbow(30,rev=True)