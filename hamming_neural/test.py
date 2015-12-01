#!/usr/bin/env python
# -- coding: utf-8 --

__author__ = 'michael'
import cv2
import sys
import numpy as np
import png
#im = cv2.imread('hamming_neural/test_words/ass.png')
#im3 = im.copy()
#gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
#blur = cv2.GaussianBlur(gray, (5, 5), 0)
#thresh = cv2.adaptiveThreshold(blur, 255, 0, 1, 99, 1)
#
##################      Now finding Contours         ###################
#
#_, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#
#samples = np.empty((0, 100))
#responses = []
#keys = [i for i in range(48, 58)]
#
#for cnt in contours:
#    if cv2.contourArea(cnt) > 50:
#        [x, y, w, h] = cv2.boundingRect(cnt)
#
#        if h > 28:
#            cv2.rectangle(im, (x, y), (x+w, y+h), (0, 0, 255), 2)
#            roi = thresh[y:y+h, x:x+w]
#            roismall = cv2.resize(roi, (10, 10))
#            print roismall
#            cv2.imshow('norm', im)
#            key = cv2.waitKey(0)
#
#            if key == 27:  # (escape to quit)
#                sys.exit()
#

r=png.Reader('hamming_neural/img/А.png')
count = 0
for i in r.read()[2]:
    print(len(i))
    count+=1

print count