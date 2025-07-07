import cv2 as cv

img = cv.imread('picture/dogs.jpg')
cv.imshow('Dogs', img)



cv.waitKey(0)