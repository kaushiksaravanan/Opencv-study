import cv2
import numpy as np
frame=np.ones([500,500,3],'uint8')*255
def click(event,x,y,flags,param):
	global pre_point,colour,pressed
	pre_point=(x,y)
	if event==cv2.EVENT_MOUSEMOVE:
		frame[y-5:y+5,x-5:x+5]=(x%255,y%255,0)
	
cv2.namedWindow("Paint")
cv2.setMouseCallback("Paint",click)
colour=(0,0,0)
line_width=3
radius=100
pre_point=(None,None)
while True:
	cv2.imshow("Paint",frame)
	ch=cv2.waitKey(1) #every 1 milli second
	if ch&0xFF==ord('q'):
		break
cv2.destroyAllWindows()
