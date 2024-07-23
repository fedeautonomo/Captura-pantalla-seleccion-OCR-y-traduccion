import os
import time

from selenium import webdriver # pip install selenium
from PIL import Image # pip install Pillow
from PIL import ImageGrab
from io import BytesIO


from matplotlib.widgets import RectangleSelector
import numpy as np
import matplotlib.pyplot as plt # pip install -U matplotlib
import matplotlib.widgets as widgets # pip install -U matplotlib
from matplotlib.widgets import EllipseSelector, RectangleSelector
plt.rcParams['toolbar'] = 'None'  # remove toolbar

import cv2 #openocr

import easyocr #pip install easyocr

from deep_translator import GoogleTranslator #pip install deep-translator

import keyboard


def onselect(eclick, erelease):
    if eclick.ydata>erelease.ydata:
        eclick.ydata,erelease.ydata=erelease.ydata,eclick.ydata
    if eclick.xdata>erelease.xdata:
        eclick.xdata,erelease.xdata=erelease.xdata,eclick.xdata
    ax.set_ylim(erelease.ydata,eclick.ydata)
    ax.set_xlim(eclick.xdata,erelease.xdata)
    fig.canvas.draw()
    fig.savefig('screenshot.jpg', bbox_inches='tight' )



#def pataplumbicus():
if __name__ == '__main__':

    jointresult = ''
    jointresult = ''
    fig = plt.figure()
    ax = fig.add_subplot(111)
    im = ImageGrab.grab()
    arr = np.asarray(im)

    plt_image = plt.imshow(arr)


    rs = widgets.RectangleSelector( ax, onselect)

    plt.axis('off')
    plt.show()
    #print("0")
    #--------------------------------------- Ya tengo la imagen
    #print("1")
    reader = easyocr.Reader(['en'])
    #print("2")
    result = reader.readtext('screenshot.jpg')
    #print("3")
   
    for res in result:
        #print(f"{res[1]}")
        jointresult = jointresult+" "+str(res[1])

    translated = GoogleTranslator(source='auto', target='es').translate(jointresult)
    print(translated)

    input("Enter para cerrar...")