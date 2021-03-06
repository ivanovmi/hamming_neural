#!/usr/bin/env python
# -- coding: utf-8 --

import setuptools

try:
    import multiprocessing  # noqa
except ImportError:
    pass

setuptools.setup(
    setup_requires=['pbr'],
    scripts=['bin/hamming-neural'],
    pbr=True)
