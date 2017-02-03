# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 19:04:07 2017
"""
import numpy
from matplotlib import pyplot

a = numpy.array([1, 2, 3])
b = a.copy()

b[1] = 7
print (a)
print(b)