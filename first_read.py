import numpy as np
import cv2

img_c = cv2.imread('images/sky.jpg',cv2.IMREAD_COLOR)
img_g = cv2.imread('images/sky.jpg',cv2.IMREAD_GRAYSCALE)
img_uc = cv2.imread('images/sky.jpg',cv2.IMREAD_UNCHANGED)

cv2.imshow('color image',img_c)
cv2.imshow('grayscale image',img_g)
cv2.imshow('unchanged image',img_uc)

cv2.waitKey(0)
cv2.destroyAllWindows()
