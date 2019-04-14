# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 17:44:47 2019

@authors: Yash Solanki, Jatna Bavshi, Saad Shaikh, Ishita Nandwani
"""
import numpy as np
import glob
from PIL import Image

def pixelProc(intensity):
    if(intensity>150):
        return intensity
    else:    
        return 0
#def pixelProcBlue(intensity):
#    return 255
#def pixelProcGreen(intensity):
#    return 255


basewidth = 200
for i in glob.glob('6.jpg'):
    im = Image.open(i)
    wpercent = (basewidth/float(im.size[0]))
    hsize = int((float(im.size[1])*float(wpercent)))
    im = im.resize((basewidth,hsize), Image.ANTIALIAS)
    im = im.convert('LA')
    im.show()
    im = im.point(pixelProc)
#    R,G,B= im.split()
#    R.show()
#    G.show()
#    B.show()
#    R = R.point(pixelProc)
#    G = G.point(pixelProc)
#    B = B.point(pixelProc)
#    R.show()
#    G.show()
#    B.show()
#    RGB = Image.merge('RGB', (R, G, B))
#    RGB.show()
    im.show()



 
