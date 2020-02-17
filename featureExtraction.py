# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 19:41:29 2020

@author: shield
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 16:08:04 2020

@author: himanshu
"""

import numpy as np
import cv2
import glob

def featureExtraction(img_path, config):
    
    x = list()
    
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
        fimg = 255 - fimg
        rsum = np.sum(fimg,axis=1)
        rsum = (rsum/128)*10
        x.append(rsum)
    return np.array(x).ravel()

config = dict()
config['ksize'] = (13,13)
config['sigma'] = 10
config['lambdaa'] = 15
config['gamma'] = 0
config['no_of_angles'] = 8
img_path = "img/2bw.png"

X = list()
y = list()

count = 0
for path in glob.glob("/media/himanshu/C2B05102B050FDFB/dataset/exp/lines/**/*.png",recursive=True):
    wid = path.split("/")[7]
    x = featureExtraction(path, config)
    X.append(x)
    y.append(wid)
    count+=1
print("count = ", count)
X = np.array(X)
y = np.array(y)
np.savez_compressed("/home/himanshu/Desktop/lines_all_gabor.npz",data = X, target = y)
    