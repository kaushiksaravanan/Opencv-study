import cv2
import numpy as np
import random
frame=np.ones([500,500,3],'uint8')*255

pressed=False
def click(event,x,y,flags,param):
	global pre_point,colour,pressed
	if event==cv2.EVENT_LBUTTONDOWN:
		#random colour 
		pressed=True
	if event==cv2.EVENT_LBUTTONUP:
		pressed=False
	pre_point=(x,y)
	c1 = random.randint(0, 255)
	c2 = random.randint(0, 255)
	c3 = random.randint(0, 255)

	if event==cv2.EVENT_MOUSEMOVE and pressed==True:
		frame[y-5:y+5,x-5:x+5]=(c1,c2,c3)
	elif event==cv2.EVENT_MOUSEMOVE and pressed==False:
		frame[y-5:y+5,x-5:x+5]=(255,255,255)
	
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
