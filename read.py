
# Reading the image

import cv2 as cv

img = cv.imread('picture/img 2_large.jpg')

cv.imshow('Dog-Cat', img)


cv.waitKey(0)

# Reading the video

capture = cv.VideoCapture('videos/20220611_135309.mp4')

while True:
     isTrue, frame = capture.read()
     cv.imshow('videos', frame)

     if cv.waitKey(20) & 0xFF==ord('d'):
         break

capture.release()
cv.destroyAllWindows()



