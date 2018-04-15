# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 10:23:15 2018

@author: asus
"""

import cv2
import os
import numpy as np

from face_detect import *

def train():
    imgData = []
    labels = []
    
    datasets = os.listdir('dataset')
    
    #print datasets
    
    for label, dataset in enumerate(datasets):
        
        path = 'dataset/' + dataset + '/train/'
        
        images = os.listdir(path)
        
        for i, image in enumerate(images):
            imgPath = path + image
            #print(i+1)
            face = faceDetect(imgPath)
            imgData.append(face)
            labels.append(label)
    
    recognizer = cv2.createLBPHFaceRecognizer()
    recognizer.train(imgData, np.array(labels))
    recognizer.save('model.yml')
    
    np.savetxt('index.txt', datasets, delimiter=" ", fmt="%s") 
    