# -*- coding: utf-8 -*

# Detect orange-colored parts in the following image,
# and mask the rest by black.

import cv2
import numpy as np

# set orange thresh

lower_blue = np.array([11, 43, 46])
upper_blue = np.array([25, 255, 255])

img = cv2.imread('aaa.jpg')

# get a frame and show

frame = img

cv2.imshow('Capture', frame)

# change to hsv model
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# get mask
mask = cv2.inRange(hsv, lower_blue, upper_blue)
cv2.imshow('Mask', mask)

# detect red
res = cv2.bitwise_and(frame, frame, mask=mask)
cv2.imshow('Result', res)

cv2.waitKey(0)
cv2.destroyAllWindows()