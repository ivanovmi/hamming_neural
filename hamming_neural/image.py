#!/usr/bin/env python
# -- coding: utf-8 --

from __future__ import division
__author__ = 'michael'

import binascii
import numpy as np
import os
from PIL import Image
import hashlib
import time
import tempfile


def convert_letter_to_bitmap(image_file, train=True):
    let_mass = []
    im = Image.open(image_file)
    im = im.resize((100, 100), Image.ANTIALIAS)
    pix = im.load()

    for x in xrange(0, im.size[0]):
        for y in xrange(0, im.size[1]):
            if train is True:
                pixel = sum(pix[x,y])/3
            else:
                pixel = pix[x,y]

            if pixel/255 >= 0.5:
                let_mass.append(1)
            else:
                let_mass.append(0)

    return let_mass


def create_target():
    target = np.ones((32, 10000), dtype=np.float)
    a = 0
    for image in sorted(os.listdir(os.path.abspath('hamming_neural/img/'))):
        target[a, :] = convert_letter_to_bitmap(os.path.abspath('hamming_neural/img/'+image), True)
        a += 1

    return target


def slice_image(imagefile):
    tmp_dir = tempfile.mkdtemp()
    im = Image.open(imagefile)
    im2 = Image.new("P", im.size, 255)
    im = im.convert("P")

    temp = {}
    for x in range(im.size[1]):
        for y in range(im.size[0]):
            pix = im.getpixel((y, x))
            temp[pix] = pix
            if pix == 0 or pix == 255:
                im2.putpixel((y, x), 0)


    inletter = False
    foundletter = False
    start = 0
    end = 0

    letters = []

    for y in range(im2.size[0]):
        for x in range(im2.size[1]):
            pix = im2.getpixel((y,x))
            if pix != 255:
                inletter = True
        if foundletter is False and inletter is True:
            foundletter = True
            start = y
        if foundletter is True and inletter is False:
            foundletter = False
            end = y
            letters.append((start, end))

        inletter=False

    count = 0

    for letter in letters:
        m = hashlib.md5()
        im3 = im2.crop((letter[0], 0, letter[1], im2.size[1]))
        im3.save(tmp_dir+"/./%s.png" % count, "PNG")
        count += 1

    return tmp_dir

#print(slice_image('/home/michael/Pictures/wtf.png'))