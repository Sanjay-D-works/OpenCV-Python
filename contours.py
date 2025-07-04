import cv2 as cv
import numpy as np

img = cv.imread('picture/img 3.jpg')
cv.imshow('CATS', img)

#1. shapes
blank = np.zeros(img.shape, dtype="uint8")
cv.imshow('Blank', blank)

# 2. Gray(cvtColor)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GRAY', gray)

#3. blur(Gaussianblur)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('BLUR', blur)

# 4. Canny

canny = cv.Canny(img, 125, 175)
cv.imshow('CANNY', canny)

# 5. Threshold

ret, thresh = cv.threshold(gray, 125,255, type=cv.THRESH_BINARY)
cv.imshow('THRESH', thresh)

# 6. contours, Hierarchies

contours, hierarchies = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

contours, hierarchies = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found!')

#drawContours

cv.drawContours(blank, contours, -1, 255, 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)
