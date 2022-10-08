#draw line to point clicked canvas

import cv2
import numpy as np
frame=np.ones([500,500,3],'uint8')*255
def click(event,x,y,flags,param):
	global pre_point,fin_point,pressed
	if event==cv2.EVENT_LBUTTONDOWN:
		pre_point=(x,y)
		
cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame",click)
colour=(0,0,0)
line_width=3
radius=100
pre_point=(None,None)
fin_point=(0,0)
while True:
	cv2.line(frame,pre_point,fin_point,colour,line_width)
	cv2.imshow("Frame",frame)
	ch=cv2.waitKey(1) #every 1 milli second
	if ch&0xFF==ord('q'):
		break
cv2.destroyAllWindows()
