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
import os
rcParams['figure.figsize'] = 8,12



def gaborFilterImages(img_path, config, dest_fol_path):
    ksize = config['ksize']
    sigma = config['sigma']
    lambdaa = config['lambdaa']
    gamma = config['gamma']
    phi = 0
    no_of_angles = config['no_of_angles']
    img = cv2.imread(img_path,0)
    
    for i in range(no_of_angles):
        theta = i * (np.pi/no_of_angles)
        kernel = cv2.getGaborKernel(ksize,sigma,theta,lambdaa,gamma,phi,ktype = cv2.CV_32F)    
        fimg = cv2.filter2D(img, cv2.CV_8UC3,kernel)
        cv2.imwrite(dest_fol_path + os.sep + str(i)+".png",fimg)
    return True




config = dict()
config['ksize'] = (13,13)
config['sigma'] = 10
config['lambdaa'] = 15
config['gamma'] = 0
config['no_of_angles'] = 8
img_path = "img/2bw.png"

gaborFilterImages(img_path,config,"/home/himanshu/Desktop")

#ksize = (13,13)
#sigma = 10
#theta = 2*(np.pi/8)
#lambd = 15
#gamma = 0
#phi = 0

#kernel = cv2.getGaborKernel(ksize,sigma,theta,lambd,gamma,phi,ktype = cv2.CV_32F)
#img = cv2.imread(img_path,0)
#fimg = cv2.filter2D(img, cv2.CV_8UC3,kernel)
##plt.imshow(cv2.cvtColor(kernel,cv2.COLOR_BGR2RGB))
#for i in range(9):
#    plt.subplot(3,3,i+1)
#    phi = i
#    kernel = cv2.getGaborKernel(ksize,sigma,theta,lambd,gamma,phi,ktype = cv2.CV_32F)
#    plt.title("phi = "+str(i))
#    plt.imshow(cv2.cvtColor(kernel,cv2.COLOR_BGR2RGB))

#plt.subplot(3,1,1)
#plt.imshow(cv2.cvtColor(kernel,cv2.COLOR_BGR2RGB))
#plt.subplot(3,1,2)
#plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
#plt.subplot(3,1,3)
#plt.imshow(cv2.cvtColor(fimg,cv2.COLOR_BGR2RGB))

#rsum = np.sum(fimg,axis=1)
#print(rsum.shape)