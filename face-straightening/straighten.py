# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 03:24:47 2018

@author: Chintan
"""

import imutils
from imutils import face_utils
import dlib
import cv2
import math
from imgaug import augmenters as iaa

def midPoint(x1, y1, x2, y2):
    return ((x2+x1)/2, (y2+y1)/2)

def dist(x1, y1, x2, y2):
    return math.hypot(x2 - x1, y2 - y1) 

features = {'jaw' : (0, 17),
            'right_eyebrow' : (17, 22),
            'left_eyebrow' : (22, 27),
            'nose' : (27, 36),
            'right_eye' : (36, 42),
            'left_eye' : (42, 48),
            'mouth' : (48, 68)}

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

image = cv2.imread('a.jpg')
image = imutils.resize(image, width = 500)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

rects = detector(image, 1)

# loop over the face detections
   
    

# determine the facial landmarks for the face region, then
# convert the landmark (x, y)-coordinates to a NumPy array
shape = predictor(image, rects)
shape = face_utils.shape_to_np(shape)
#print(shape)

jaw = features['jaw']
pts = shape[jaw[0]:jaw[1]]

#finding nasal length
nose = features['nose']
pts = shape[nose[0]:nose[1]]
x1, y1 = pts[0, 0], pts[0, 1]
pts = shape[jaw[0]:jaw[1]]
x2, y2 = pts[8, 0], pts[8, 1]

dimg = iaa.Sequential([
    iaa.Affine(rotate=(90-(math.atan2(y2-y1,x2-x1))*180/math.pi)) 
]).augment_images([image])
image = dimg[0]

#print(pts)
rects = detector(image, 1)
shape = predictor(image, rects)
shape = face_utils.shape_to_np(shape)
jaw = features['jaw']
pts = shape[jaw[0]:jaw[1]]
x1, y1, x2, y2 = pts[0][0], pts[0][1], pts[-1][0], pts[-1][1]
cv2.line(image, (x1,y1), (x2,y2), (255,0,0), 1)

rbrow = features['right_eyebrow']
pts = shape[rbrow[0]:rbrow[1]]
x1, y1 = pts[2][0], pts[2][1]
lbrow = features['left_eyebrow']
pts = shape[lbrow[0]:lbrow[1]]
x2, y2 = pts[2][0], pts[2][1]
x1, y1 = midPoint(x1, y1, x2, y2)
pts = shape[jaw[0]:jaw[1]]
x2, y2 = pts[8][0], pts[8][1]
cv2.line(image, (x1,y1), (x2,y2), (0,255,0), 1)
    
cv2.imshow("Image", image)       
cv2.waitKey(0)