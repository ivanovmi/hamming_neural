#!/usr/bin/env python
# -- coding: utf-8 --

import neurolab
import numpy as np
import pprint
__author__ = 'michael'

target = np.ones((10, 15), dtype=np.float)

target[0, :] = np.array([1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1])
target[1, :] = np.array([0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0])
target[2, :] = np.array([1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1])
target[3, :] = np.array([1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1])
target[4, :] = np.array([1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1])
target[5, :] = np.array([1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1])
target[6, :] = np.array([1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1])
target[7, :] = np.array([1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1])
target[8, :] = np.array([1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1])
target[9, :] = np.array([1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1])

# Create and train network
neuron = neurolab.net.newhem(target, neurolab.trans.SatLinPrm(1,0,100),1000)
neuron.sim(target)

for symbol in xrange(0, len(target)):
    input = target[symbol]#[[1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1]]
    output = neuron.sim([input])
    print("Outputs on neuron "+str(symbol)+":")
    for i in xrange(0, len(output[0])):
        print 'element {0}: {1}'.format(i, output[0][i])
    print "\n"*2
