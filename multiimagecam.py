#!/usr/bin/python3
import cv2

#0xffto capture keyboard
# starting cmera
cap=cv2.VideoCapture(0)
while cap.isOpened():
	status,frame=cap.read()

	#converting image in gray scale
	graying=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	print(frame.shape)
	# we can draw all those patterns
	#line
	# starting coordinate ,ending,color,data
	cv2.line(frame,(0,0),(200,300),(0,255,0),3)
	#rectangle
	#cv2.rectangle(frame,(50,50),(400,350),(0,0,250),3)
	#circle
	cv2.circle(frame,(150,250),100,(13,44,123),3)
	#for type
	font=cv2.FONT_HERSHEY_SIMPLEX
	#                                       size ,color,line thickness of letter 
	cv2.putText(frame,"OpenCV",(10,50),font,2,(0,0,255),2,cv2.LINE_AA)
	cv2.imshow('live',frame)
	#cv2.imshow('livegraying',graying)
	if cv2.waitKey(10) & 0xff == ord('q'):
		break

#cv2.destroyWindow('live')
cv2.destroyAllWindows() # this will destroy all windows


#to close the release
cap.release() 
