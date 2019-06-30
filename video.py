#!/usr/bin/python3
import cv2

#0xffto capture keyboard
# starting cmera
cap=cv2.VideoCapture(0)
# adding plugin
plugin=cv2.VideoWriter_fourcc(*'XVID')
#saving video
# name of the file,plugin name, no of frames per second , width height frame sizee of video where to write
# file to write the video 
output=cv2.VideoWriter('clss.avi',plugin,20,(640,480))

while cap.isOpened():
	status,frame=cap.read()
	cv2.imshow('live',frame)
	output.write(frame) # for write in video writer
	if cv2.waitKey(10) & 0xff == ord('q'):
		break
	

#cv2.destroyWindow('live')
cv2.destroyAllWindows() # this will destroy all windows


#to close the release
cap.release() 
