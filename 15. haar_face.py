import cv2 as cv

img = cv.imread('picture/cutie 2.jpg')
cv.imshow('cutie', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray person', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)

print(f'Number of faces found = {len(faces_rect)}')

for x,y,z,h in faces_rect:
    cv.rectangle(img,(x,y),(x+z,y+h),(255,0,0),2)

cv.imshow('Detected faces', img)

img = cv.imread('picture/people.jpg')
cv.imshow('Group of people', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray person', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2)

print(f'Number of faces found = {len(faces_rect)}')

for x,y,z,h in faces_rect:
    cv.rectangle(img,(x,y),(x+z,y+h),(255,0,0),2)

cv.imshow('Detected faces', img)

cv.waitKey(0)