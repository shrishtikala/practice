#!/usr/bin/python3
import cv2

# starting cmera
cap=cv2.VideoCapture(0)
# first camera
# to check camera is started or not

if cap.isOpened():
	print("camera ready")
else:
	print(no)
status,img=cap.read()
cv2.imshow('liveimage',img)
cv2.waitKey(0)
