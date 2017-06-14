import numpy as np
import cv2
from matplotlib import pyplot as plt

#Read Image in different mode
img_c = cv2.imread('images/sky.jpg',cv2.IMREAD_COLOR)
img_g = cv2.imread('images/sky.jpg',cv2.IMREAD_GRAYSCALE)
img_uc = cv2.imread('images/sky.jpg',cv2.IMREAD_UNCHANGED)

#Show Image
cv2.imshow('color image',img_c)
cv2.imshow('grayscale image',img_g)
cv2.imshow('unchanged image',img_uc)

#Use matplot
plt.imshow(img_g, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
plt.imshow(img_g, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
plt.imshow(img_g, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

#Wait any key pressed and save that key
key = cv2.waitKey(0)

#if esc
if key == 27 :
    #Close all windows
    cv2.destroyAllWindows()
#if s
elif key == ord('s') :
    #Save image
    cv2.imwrite('outputs/sky_color.jpg',img_c)
    cv2.imwrite('outputs/sky_gray.jpg',img_g)
    cv2.imwrite('outputs/sky_unchange.jpg',img_uc)
    #Close all windows
    cv2.destroyAllWindows()
