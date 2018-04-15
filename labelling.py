# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 00:12:34 2018

@author: Chintan
"""

import os
import face_detect_new as fd

def prep(dataPath):
    faces = []
    labels = []
    
    dirs = os.listdir(dataPath)
    
    i = 0
    for dir_name in dirs:
        label = i
        i = i + 1
        src = dataPath + '/' + dir_name + '/' + 'train'
        images = os.listdir(src)
        for img in images:
#            image = cv2.imread(src + '/' + img)
#            cv2.imshow("test", image)
#            cv2.waitKey(0)
            face = fd.detectFace(src + '/' + img)
            
            if face is not None:
                faces.append(face)
                labels.append(label)
#            cv2.destroyAllWindows()
#            cv2.waitKey(1)
#            cv2.destroyAllWindows()
    return faces, labels
            
        