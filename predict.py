# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 11:29:34 2018

@author: asus
"""

from face_detect import *
import cv2

def predict(imgPath):
    
    labels = open('index.txt').read().split()
    #print(labels)
    
    recognizer = cv2.createLBPHFaceRecognizer()
    recognizer.load('model.yml')
    
    face = faceDetect(imgPath)
    label, score = recognizer.predict(face)
    
    #print(label, score)
    
    return label, labels[label]