import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('picture/img 4.jpg')
cv.imshow('img', img)

# plt.imshow(img)
# plt.show()

# 1. BGR to greyscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# 2. BGR to HSV

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)


# 3. BGR to L*A*B

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# 4. BGR to RGB

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# plt.imshow(img)
# plt.show()

# HSV to BGR

bgr = cv.cvtColor(img, cv.COLOR_HSV2BGR)
cv.imshow('BGR', bgr)

lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB --> BGR', lab_bgr)

cv.waitKey(0)

