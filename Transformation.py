import cv2 as cv
import numpy as np

img = cv.imread('picture/img 5.jpg')

cv.imshow('Dog-Cat', img)

#Translation (warpAffine).
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translate = translate(img, -100, 100)
cv.imshow('Translate', translate)

# Roatation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width/2, height/2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img,45)
cv.imshow('Rotated', rotated)

rotated_rotated = rotate()
rotated_rotated = rotate()

cv.waitKey(0)

