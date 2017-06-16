import cv2
import numpy as np                           #importing libraries

def de_bg(frame) :
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    ret,thresh1 = cv2.threshold(blur,70,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    return thresh1

cap = cv2.VideoCapture(0)                #creating camera object

while( cap.isOpened() ) :
    ret,img = cap.read()                         #reading the frames
    cv2.imshow('input',de_bg(img))                  #displaying the frames
    k = cv2.waitKey(10)
    if k == 27:
        break
