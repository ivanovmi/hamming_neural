#!/usr/bin/env python
# -- coding: utf-8 --

__author__ = 'michael'

from PIL import Image

#img = Image.open('img/a.png').convert('L')
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.patches as mpatches

im1 = Image.open('img/a.png')

# Flip the .tif file so it plots upright
#im1 = im.transpose(Image.FLIP_TOP_BOTTOM)

# Plot the image
plt.imshow(im1)
ax = plt.gca()

# create a grid
ax.grid(True, color='r', linestyle='--', linewidth=2)
# put the grid below other plot elements
ax.set_axisbelow(True)

# Draw a box
xy = 200, 200,
width, height = 100, 100
ax.add_patch(mpatches.Rectangle(xy, width, height, facecolor="none",
    edgecolor="blue", linewidth=2))

plt.draw()

plt.show()