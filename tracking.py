import numpy as np
import cv2

cap = cv2.VideoCapture(0)
tracker = cv2.Tracker_create("MIL")

ret, frame = cap.read()

box = (287, 23, 86, 320)

tracker.init(frame,box)

while(1):
    ret, frame = cap.read()

    ret, box = tracker.update(frame)

    if ret:
        p1 = (int(box[0]), int(box[1]))
        p2 = (int(box[0] + box[2]), int(box[1] + box[3]))
        cv2.rectangle(frame, p1, p2, (0,255,255),10)

    cv2.imshow('frame',frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
