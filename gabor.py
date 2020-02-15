#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 16:08:04 2020

@author: himanshu
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt
from pylab import rcParams
rcParams['figure.figsize'] = 25, 8

ksize = (10,10)
sigma = 5
theta = 1*(np.pi/3)
lambd = 9
gamma = 0
phi = 0

kernel = cv2.getGaborKernel(ksize,sigma,theta,lambd,gamma,phi,ktype = cv2.CV_32F)
img = cv2.imread("img/1.png")
print(img.shape)
fimg = cv2.filter2D(img, cv2.CV_8UC3,kernel)
plt.subplot(3,1,1)
plt.imshow(cv2.cvtColor(kernel,cv2.COLOR_BGR2RGB))
plt.subplot(3,1,2)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.subplot(3,1,3)
plt.imshow(cv2.cvtColor(fimg,cv2.COLOR_BGR2RGB))