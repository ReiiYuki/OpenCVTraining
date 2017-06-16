import numpy as np
import cv2

cap = cv2.VideoCapture(0)

fgbg = cv2.createBackgroundSubtractorMOG2()
'''ret,  lsframe = cap.read()
lsframe = cv2.cvtColor(lsframe,cv2.COLOR_BGR2GRAY)
#sp = initframe.shape
af = np.zeros(lsframe.shape)'''
while(1):
    '''af[:] = 0
    for i in range(5):
        ret, frame = cap.read()
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        frame = cv2.GaussianBlur(frame,(5,5),0)
        af = frame+af
    '''
    ret, frame = cap.read()
    # frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # af = frame+af
    # ret, frame = cap.read()
    # frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # af = frame+af
    #print type(frame)
    fgmask = fgbg.apply(frame)
# #
# '''    o = np.abs(frame - lsframe)
#     th = np.percentile(o,99)
#     o[o<th] = 0
#     cv2.imshow('frame',o)
#     lsframe[:] = af'''
    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
