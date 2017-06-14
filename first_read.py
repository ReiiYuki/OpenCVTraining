import numpy as np
import cv2

#Read Image in different mode
img_c = cv2.imread('images/sky.jpg',cv2.IMREAD_COLOR)
img_g = cv2.imread('images/sky.jpg',cv2.IMREAD_GRAYSCALE)
img_uc = cv2.imread('images/sky.jpg',cv2.IMREAD_UNCHANGED)

#Show Image
cv2.imshow('color image',img_c)
cv2.imshow('grayscale image',img_g)
cv2.imshow('unchanged image',img_uc)

#Wait any key pressed
cv2.waitKey(0)
#Close all windows
cv2.destroyAllWindows()
