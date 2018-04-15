# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 09:45:52 2018

@author: Chintan
"""

import cv2
from imgaug import augmenters as iaa

def alter(img):
    srcPath = 'original/'
    destPath = 'depricated/'
    image = cv2.imread(srcPath + img)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    dimg = iaa.Sequential([
        iaa.Fliplr(1) 
    ]).augment_images([image])
    cv2.imwrite(destPath + img[:-4] + '_flipped.jpg', dimg[0])
    
    dimg = iaa.Sequential([
        iaa.Crop(px=(8, 0, 0, 32)), 
    ]).augment_images([image])
    cv2.imwrite(destPath + img[:-4] + '_cropped.jpg', dimg[0])
    
    dimg = iaa.Sequential([
        iaa.GaussianBlur(sigma=(0, 3.0)) 
    ]).augment_images([image])
    cv2.imwrite(destPath + img[:-4] + '_blurred.jpg', dimg[0])
    
    for i in range(-45,45,15):
        dimg = iaa.Sequential([
                iaa.Add(i)
        ]).augment_images([image])
        cv2.imwrite(destPath + img[:-4] + '_b_'+ str(i) + '.jpg', dimg[0])
        
        dimg = iaa.Sequential([
                iaa.Add((i-10, i+10), per_channel=True)
        ]).augment_images([image])
        cv2.imwrite(destPath + img[:-4] + '_bpc_'+ str(i) + '.jpg', dimg[0])
        
#        dimg = iaa.Sequential([
#                iaa.AddToHueAndSaturation(i)
#        ]).augment_images([image])
#        cv2.imwrite(destPath + img[0] + '_hue_'+ str(i) + '.jpg', dimg[0])
        
        dimg = iaa.Sequential([
                iaa.Multiply((i+90)*0.0056)
        ]).augment_images([image])
        cv2.imwrite(destPath + img[:-4] + '_mul_'+ str(i) + '.jpg', dimg[0])
        
        dimg = iaa.Sequential([
                iaa.Multiply(((i+90)*0.0056 - 0.10, (i+90)*0.0056 + 0.10), per_channel=True)
        ]).augment_images([image])
        cv2.imwrite(destPath + img[:-4] + '_mulpc_'+ str(i) + '.jpg', dimg[0])
        
        dimg = iaa.Sequential([
                iaa.ContrastNormalization((i+90)*0.0112 + 0.225)
        ]).augment_images([image])
        cv2.imwrite(destPath + img[:-4] + '_cn_'+ str(i) + '.jpg', dimg[0])

        dimg = iaa.Sequential([
                iaa.ContrastNormalization(((i+90)*0.0112 + 0.225 - 0.10, (i+90)*0.0112 + 0.225 + 0.10), per_channel=True)
        ]).augment_images([image])
        cv2.imwrite(destPath + img[:-4] + '_mpcn_'+ str(i) + '.jpg', dimg[0])
        
        dimg = iaa.Sequential([
                iaa.Add(i),
                iaa.Add((i-10, i+10), per_channel=True),
                iaa.Fliplr(1),
                iaa.Crop(px=(8, 0, 0, 32)),
                #iaa.AddToHueAndSaturation(i),
                iaa.Multiply((i+90)*0.0056),
                iaa.Multiply(((i+90)*0.0056 - 0.10, (i+90)*0.0056 + 0.10), per_channel=True),
                iaa.ContrastNormalization((i+90)*0.0112 + 0.225),
                iaa.ContrastNormalization(((i+90)*0.0112 + 0.225 - 0.10, (i+90)*0.0112 + 0.225 + 0.10), per_channel=True)
        ]).augment_images([image])
        cv2.imwrite(destPath + img[:-4] + '_mix_'+ str(i) + '.jpg', dimg[0])
    #cv2.imshow("a", images_aug[0][0])
    #cv2.waitKey(0)