# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 13:46:07 2018

@author: asus
"""

import pandas as pd
from predict import *
from conversion import decode
import cv2

def make_db():
    df = pd.read_csv('database/main.csv')
    print(df)
    
    ref = pd.read_csv('database/aadhar.csv')
    #print(ref)
    
    name = 'aadhar'
    
    for i, row in ref.iterrows():   
            img = row['image']
            img = decode(img)
            cv2.imwrite('temp.jpg', img)
            label, lblname = predict('temp.jpg')
            print(lblname)
            #print(df[name][label])
            df[name][label] = row['id']         
        
    print(df)