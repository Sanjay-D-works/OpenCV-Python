import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('picture/img 1.jpg')
cv.imshow('Dogs', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Mask', masked)

#Grayscale histogram

gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('Number of pixels')
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()

# Color histogram

colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.figure()
    plt.title('Colour Histogram')
    plt.xlabel('Bins')
    plt.ylabel('Number of pixels')
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
plt.show()




cv.waitKey(0)