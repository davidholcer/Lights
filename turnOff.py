#!/usr/bin/env python3

from light import *

# Find the first BlinkStick
bstick = blinkstick.find_first()


def turnOff():
    setColor("#0", bstick, start=0, end=32)

turnOff()
