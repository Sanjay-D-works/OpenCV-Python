import cv2 as cv

img = cv.imread('picture/img 2.jpg')
cv.imshow('Cats', img)

# 1. Averaging
average = cv.blur(img, (7,7))
cv.imshow('Average Blur', average)

# 2. Gaussian Blur
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gauss)

# 3. Median blur
median = cv.medianBlur(img, 7)
cv.imshow('Median Blur', median)

# 4. Bilateral
bilateral = cv.bilateralFilter(img, 10, 15, 15)
cv.imshow('Bilateral Blur', bilateral)

cv.waitKey(0)