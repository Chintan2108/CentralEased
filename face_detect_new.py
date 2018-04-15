# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 20:57:23 2018

@author: Chintan
"""
import cv2, imutils

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

def detectFace(imgPath, disp = False):
    global faceCascade
    
    image = cv2.imread(imgPath)
    image = imutils.resize(image, width=500)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(image, 
                                         scaleFactor=1.2, 
                                         minNeighbors=5,
                                         minSize = (50, 50),
                                         flags = cv2.CASCADE_SCALE_IMAGE
                                        )
    

    if(len(faces) == 0):
        return None
    
    (x,y,w,h) = faces[0]
    face = image[y: y + w, x: x + h]
    
    if disp == True:
        name = imgPath.split('/')[-1]
        cv2.namedWindow(name, 500)
        cv2.imshow(name, face)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    return face
