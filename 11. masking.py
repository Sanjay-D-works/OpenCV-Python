import cv2 as cv
import numpy as np

img = cv.imread('picture/img 2.jpg')
cv.imshow('Original Image', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)

mask = cv.circle(blank, (img.shape[1]//2 + 45, img.shape[0]//2 + 45), 100, 255, -1)
cv.imshow('Mask', mask)

masking = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked Image', masking)

mask = cv.rectangle(blank, (img.shape[1]//2 + 45, img.shape[0]//2 + 45),
                    (img.shape[1]//2 +100, img.shape[0]//2 + 100), 100, 255, -1)
cv.imshow('Mask', mask)

circle = cv.circle(blank.copy(), (img.shape[1]//2 + 45, img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', mask)

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow('Weird_shape', weird_shape)

masking = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow('Weird Masked Image', masking)

masking = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked Image', masking)



cv.waitKey(0)