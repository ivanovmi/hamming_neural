#!/usr/bin/env python
# -- coding: utf-8 --

from __future__ import division
__author__ = 'michael'

import binascii
import numpy as np
import os
from PIL import Image


def convert_letter_to_bitmap(image_file):
    let_mass = []
    im = Image.open(image_file)
    im = im.resize((100, 100), Image.ANTIALIAS)
    pix = im.load()

    for x in xrange(0, im.size[0]):
        for y in xrange(0, im.size[1]):
            if sum(pix[x, y])/3/255 >= 0.5:
                let_mass.append(1)
            else:
                let_mass.append(0)

    return let_mass


def create_target():
    target = np.ones((32, 10000), dtype=np.float)
    a = 0
    for image in sorted(os.listdir(os.path.abspath('hamming_neural/img/'))):
        target[a, :] = convert_letter_to_bitmap(os.path.abspath('hamming_neural/img/'+image))
        a += 1

    return target


#try:
#    # pick an image file you have in the working directory
#    # or give the full file path ...
#    image_file = 'py.ico'
#    fin = open(image_file, "rb")
#    data = fin.read()
#    fin.close()
#except IOError:
#    print("Image file %s not found" % image_file)
#    raise SystemExit
## convert every byte of data to the corresponding 2-digit hexadecimal
#hex_str = str(binascii.hexlify(data))
## now create a list of 2-digit hexadecimals
#hex_list = []
#bin_list = []
#for ix in range(2, len(hex_str)-1, 2):
#    hex = hex_str[ix]+hex_str[ix+1]
#    hex_list.append(hex)
#    bin_list.append(bin(int(hex, 16))[2:])
##print(bin_list)
#bin_str = "".join(bin_list)
#print(bin_str)