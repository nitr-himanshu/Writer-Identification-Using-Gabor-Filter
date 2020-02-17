# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 19:13:37 2020

@author: shield
"""

from PIL import Image
import glob

def compress(img_path, new_height, inplace=True, new_img_path=""):
    '''
    :param
        img_path
        new_height
        inplace(optional)
        new_img_path (required when inplace=false)
    :return
        new file path
    '''
    img = Image.open(img_path)
    hpercent = (new_height / float(img.size[1]))
    wsize = int((float(img.size[0]) * float(hpercent)))
    img = img.resize((wsize, new_height), Image.ANTIALIAS)
    if(inplace):
        new_img_path = img_path
    img.save(new_img_path)
    return new_img_path

for path in glob.glob("/media/himanshu/C2B05102B050FDFB/dataset/exp/lines/**/*.png",recursive=True):
    compress(path, 128)
print("Done")
