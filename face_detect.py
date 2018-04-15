# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 23:12:20 2018

@author: asus
"""

import cv2
import imutils

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

def faceDetect(imgPath, disp = False):   
    
    global faceCascade
    
    image = cv2.imread(imgPath)
    image = imutils.resize(image, width=500)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("", image)
    #cv2.waitKey(0)
    
    #faces = faceCascade.detectMultiScale(image)
    
    faces = faceCascade.detectMultiScale(
                image,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(50, 50),
                flags = cv2.cv.CV_HAAR_SCALE_IMAGE,
                outputRejectLevels = True
            )

    #print(len(faces))

    (x, y, w, h) = faces[0]
    
    face = image[y: y + h, x: x + w]
    
    if disp == True:
        name = imgPath.split('/')[-1]
        cv2.namedWindow(name, 500)
        cv2.imshow(name, face)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    return face
