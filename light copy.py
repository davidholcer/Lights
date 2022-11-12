#!/usr/bin/env python3

import imageio
import scipy.cluster
import scipy.misc
import scipy
from PIL import Image
from blinkstick import blinkstick
from PIL import ImageGrab
import numpy as np
import time
import binascii
import copy
from colour import Color
startTime = time.time()
# Import blinkstick module
# Find the first BlinkStick
bstick = blinkstick.find_first()


def getAverageColor():
    image = ImageGrab.grab()
    print(type(image))
    values = []
    # for i in range(1,100):
    i = 4
    total = 0
    r = []
    g = []
    b = []
    for y in range(0, 1080, i):
        for x in range(0, 1920, i):
            color = image.getpixel((x, y))
            r.append(color[0])
            g.append(color[1])
            b.append(color[2])
            total += 1
    r = int(sum(r) / total)
    g = int(sum(g) / total)
    b = int(sum(b) / total)
    #    print(r,g,b)
    values = [r, g, b]
    hex = ('#%02x%02x%02x' % (values[0], values[1], values[2]))
    return hex


def sortBySat(colors):
    '''
    Inputs an array of colors and returns the same array sorted by saturation•brightness.
    '''
    # colors=['#333531', '#1c1c1c', '#66756e', '#7c5b1c', '#000101']
    # colors=['#f8f8f7', '#232322', '#e9e5e1', '#696d5b', '#b1afad']
    # colors=['#fefefe', '#191919', '#296437', '#f0eed6', '#8ba899']
    sXb = []
    for each in colors:
        col = Color(each)
        col = col.hsl
        # print(col)
        sXb.append(col[1] * col[2])
    sXb = np.array(sXb)
    # print(sXb)
    arrInds = sXb.argsort()
    colors = np.array(colors)
    return colors[arrInds[::-1]]
# sortBySat([])

# Set the color red on the 12th LED of R channel
# bstick.set_color(channel=0, index=14, hex="#0")


def setColor(color, bstick, start, end):
    DELAY = 0.001
    for i in range(start, end):
        try:bstick.set_color(channel=0, index=i, hex=color)
        except:pass
        time.sleep(DELAY)
    return


#from __future__ import print_function
#import binascii
#import struct

#import time

# bonus: save image using only the N most common colours


def screenColorGrabber(save=False, NUM_CLUSTERS=5, rgb=False,DEBUG=False):
    startTime = time.time()
    colors = []

   # print('reading image')
    im = ImageGrab.grab()
    im = im.resize((160, 90))      # optional, to reduce time
    ar = np.asarray(im)
    shape = ar.shape
    ar = ar.reshape(scipy.product(shape[:2]), shape[2]).astype(float)

   # print('finding clusters')
    codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)
    codes = codes.astype(int)
    #print('cluster centres:\n', codes)

    vecs, dist = scipy.cluster.vq.vq(ar, codes)         # assign codes
    counts, bins = scipy.histogram(vecs, len(codes))    # count occurrences
   # print(counts)
    index_max = scipy.argmax(counts)                    # find most frequent

    # sorts by order of frequency
    arrInds = counts.argsort()
    codesSorted = codes[arrInds[::-1]]

    for i in range(len(codes)):
        # print(i)
        ccolor = codesSorted[i]
        colour = binascii.hexlify(bytearray(int(c)
                                            for c in ccolor)).decode('ascii')
        hexx = colour[:-2]
        colors.append(hexx)

    peak = codes[index_max]
    colour = binascii.hexlify(bytearray(int(c) for c in peak)).decode('ascii')
    hexx = colour[:-2]

    # print('Most Frequent is %s (#%s)' % (peak, hexx))

    c = 0
    while c < len(colors):
        colors[c] = "#" + colors[c]
        c += 1

   # print("Colors:",colors)

    # sort the colors by saturation•brightness
    colsXSat = sortBySat(colors)
    topColor = (colsXSat[0])
    if DEBUG:
        print("Top Color (by Sat)", topColor)
        print("Colors by Sat:", colsXSat)
        print("Total Time:", time.time() - startTime, "seconds")
    # for color in colors:
    #   ColoredSquare(color)

   # print("\nBy Order of Frequency:")
   # ColoredSquares(colors)

    # PRINT SQUARE SHOWING TOP COLORS BY SATURATION
    #print("\nBy Saturation * Brightness:")
    #ColoredSquares(colsXSat)



    if rgb == True:
        setColor(topColor, bstick, 14, 32)

    if save == True:
        now = datetime.now()
        # dd/mm/YY H:M:S
        dt_string = now.strftime("_%d_%m_%Y_%H_%M_%S")

        c = ar.copy()
        for i, code in enumerate(codes):
            c[scipy.r_[scipy.where(vecs == i)], :] = code
        imageio.imwrite("./clusters%s.png" % dt_string,
                        c.reshape(*shape).astype(np.uint8))
        print('saved clustered image')

    return(topColor)


startTime = time.time()

import matplotlib
import matplotlib.pyplot as plt

def ColoredSquare(hexx):
    #getAverageColor()
    fig = plt.figure()
    fig.set_figheight(2)
    fig.set_figwidth(2)
    plt.axes()
    rectangle = plt.Rectangle((0,0), 10, 10, fc=hexx)
    fig.gca().add_patch(rectangle)
    plt.axis('off')
    plt.show()

def ColoredSquares(colors):
    #getAverageColor()
    fig, ax = plt.subplots(1,figsize=(12,7.5))
    #fig, ax = plt.subplots()

    c=0
    while c<len(colors):
        #print(colors[c])
        #print(10*c)
        rectangle = plt.Rectangle((10*c,0), 10, 10, fc=colors[c])
        ax.add_patch(rectangle)
        c+=1

    plt.xlim(0,10*len(colors))
    plt.ylim((0,10))
    plt.axis('off')
    plt.show()

    #!pip install colour

def inBetween(color1, color2,many=3):
    color1 = Color(color1)
    colors = list(color1.range_to(Color(color2),many))
#    print (colors)
   # print (', '.join(p.hex for p in colors) )
    colors=[color.hex for color in colors]
#    return (colors[1].hex)
    return colors
