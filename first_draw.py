import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)
# Draw a diagonal blue line with thickness of 5 px
# Target Image , First Point , Second Point , RGB, Thickness
cv2.line(img,(0,0),(511,511),(255,0,0),5)

# Draw rectangle
# Target Image, Top Left Point , Bottom Right Point, RGB , Thick of Line
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

# Draw Circle
# Taget Image , Center Point , Radius , RGB , Thickness / -1 mean fill
cv2.circle(img,(447,63), 63, (0,0,255), -1)

# Draw Ellipse
# Target Image , Center Point , (Lenght X , Length Y),Rotation, Start Angle , End Angle,RGB , Thickness
cv2.ellipse(img,(256,256),(100,50),0,0,180,(0,255,255),-1)

# Draw Polygon
# Point
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
# Change Shape of Array into rowx1x2
pts = pts.reshape((-1,1,2))
#   Draw Polygon from points
cv2.polylines(img,[pts],True,(0,255,255))

# Draw Text
# Import Font
font = cv2.FONT_HERSHEY_SIMPLEX
# Target Image , Word, Position , font , scale, rgb, thickness, line type
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

# Show image
cv2.imshow('color image',img)

#Wait any key pressed and save that key
key = cv2.waitKey(0)

#if esc
if key == 27 :
    #Close all windows
    cv2.destroyAllWindows()
#if s
elif key == ord('s') :
    #Save image
    cv2.imwrite('outputs/out_draw.jpg',img)
    #Close all windows
    cv2.destroyAllWindows()
