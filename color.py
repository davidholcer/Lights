#!/usr/bin/env python3

from light import *
import sys 
import time

start_time = time.time()
colorr=sys.argv[1]
#time in sec
pTime=15

while True:
    
    setColor(colorr,bstick,0,end=32)