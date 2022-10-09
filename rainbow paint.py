import cv2
import numpy as np
frame=np.ones([500,500,3],'uint8')*255
def click(event,x,y,flags,param):
	# print(event)
	# print(cv2.EVENT_MOUSEMOVE)
	global pre_point,colour,pressed
	pre_point=(x,y)
	# pre_point=(x,y)
	# cv2.circle(frame,pre_point,radius,colour,line_width)
	# if event==cv2.EVENT_LBUTTONDOWN:
	# 	frame[y-5:y+5,x-5:x+5]=(255,255,255)
		

	# 	cv2.circle(frame,pre_point,radius,colour,line_width)
		
	# if event==cv2.EVENT_RBUTTONDOWN:
	# 	colour=(0,0,255)
	# 	pre_point=(x,y)
	# 	cv2.circle(frame,pre_point,radius,colour,line_width)
		
	
	# if event==cv2.EVENT_LBUTTONUP:
	# 	colour=(255,0,0)
	# 	pre_point=(x,y)
	
	if event==cv2.EVENT_MOUSEMOVE:
		frame[y-5:y+5,x-5:x+5]=(x%255,y%255,0)

	# if event==cv2.EVENT_RBUTTONUP:
	# 	colour=(0,255,255)
	# 	pre_point=(x,y)	
		
cv2.namedWindow("Paint")
cv2.setMouseCallback("Paint",click)
colour=(0,0,0)
line_width=3
radius=100
pre_point=(None,None)
while True:
	# cv2.circle(frame,pre_point,radius,colour,line_width)
	cv2.imshow("Paint",frame)
	ch=cv2.waitKey(1) #every 1 milli second
	if ch&0xFF==ord('q'):
		break
cv2.destroyAllWindows()
