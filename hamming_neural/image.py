#!/usr/bin/env python
# -- coding: utf-8 --

from __future__ import division
__author__ = 'michael'

import binascii
import numpy as np
import os
from PIL import Image
import tempfile
from scipy.misc import toimage


def convert_letter_to_bitmap(image_file, train=True):
    let_mass = []
    im = Image.open(image_file)
    im = im.resize((100, 100), Image.ANTIALIAS)
    pix = im.load()

    for x in xrange(0, im.size[0]):
        for y in xrange(0, im.size[1]):
            if train is True:
                pixel = sum(pix[x, y])/3
            else:
                pixel = pix[x, y]

            if pixel/255 >= 0.5:
                let_mass.append(1)
            else:
                let_mass.append(0)

    return let_mass


def delete_white_lines(image):
    im = image
    im = im.resize((100, 100), Image.ANTIALIAS)
    pix = im.load()
    res_mass = []
    for x in xrange(0, im.size[0]):
        new_mass = []
        for y in xrange(0, im.size[1]):
            pixel = pix[x, y]
            new_mass.append(pixel/255)
        res_mass.append(new_mass)

    res_mass = np.array(res_mass)
    marks = []
    for i in xrange(0, 100):
        if sum(res_mass[:, i]) == 100:
            marks.append(i)
    print marks
    if marks == [] :
        return image#.rotate(180)
    else:
        for i in reversed(marks):
            res_mass = np.delete(res_mass, i, 1)

        return toimage(res_mass).transpose(Image.FLIP_LEFT_RIGHT)#.rotate(90)


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
        im3 = im2.crop((letter[0], 0, letter[1], im2.size[1]))
        im3 = delete_white_lines(im3)
        im3.save(tmp_dir+"/./%s.png" % count, "PNG")
        count += 1
    print tmp_dir
    return tmp_dir



#delete_white_lines(Image.open('/home/michael/PycharmProjects/hamming_neural/11.png')).save('test.png')