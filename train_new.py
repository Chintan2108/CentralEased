# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 01:04:57 2018

@author: Chintan
"""

import labelling as lb
import cv2
import numpy as np

FaceRecognizer = cv2.LBPHFaceRecognizer_create()

def train():
    global FaceRecognizer
    
    faces, labels = lb.prep('heroes')
    FaceRecognizer.train(faces, np.array(labels))

def predict(img):
    global FaceRecognizer
    
    label = FaceRecognizer.predict()
    print(label)
    
#print('faces %d' %len(faces))
#print('labels %d ' %len(labels))

