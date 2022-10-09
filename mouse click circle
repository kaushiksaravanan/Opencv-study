#Left mouse to draw red circle and blue circle with right mouse click

import cv2
import numpy as np
frame=np.ones([500,500,3],'uint8')*255
def click(event,x,y,flags,param):
	global pre_point,colour,pressed
	# pre_point=(x,y)
	# cv2.circle(frame,pre_point,radius,colour,line_width)
	if event==cv2.EVENT_LBUTTONDOWN:
		pre_point=(x,y)
		colour=(255,0,0)
		cv2.circle(frame,pre_point,radius,colour,line_width)
		
	if event==cv2.EVENT_RBUTTONDOWN:
		colour=(0,0,255)
		pre_point=(x,y)
		cv2.circle(frame,pre_point,radius,colour,line_width)
		
	
	# if event==cv2.EVENT_LBUTTONUP:
	# 	colour=(255,0,0)
	# 	pre_point=(x,y)
	
	# if event==cv2.EVENT_MOUSEMOVE:
	# 	colour=(255,255,0)
	# 	pre_point=(x,y)

	# if event==cv2.EVENT_RBUTTONUP:
	# 	colour=(0,255,255)
	# 	pre_point=(x,y)	
		
cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame",click)
colour=(0,0,0)
line_width=3
radius=100
pre_point=(None,None)
while True:
	# cv2.circle(frame,pre_point,radius,colour,line_width)
	cv2.imshow("Frame",frame)
	ch=cv2.waitKey(1) #every 1 milli second
	if ch&0xFF==ord('q'):
		break
cv2.destroyAllWindows()
