import cv2
import numpy as np
# frame=np.ones([500,500,3],'uint8')*255

def click(event,x,y,flags,param):
	# print(event)
	# print(cv2.EVENT_MOUSEMOVE)
	global pre_point,colour,pressed,frame
	# pre_point=(x,y)
	# print(pre_point)
	if event==cv2.EVENT_MOUSEMOVE:
		colour=(x%255,y%255,(x+y)%255)
		pre_point=(x,y)	
		
cv2.namedWindow("Paint")
cv2.setMouseCallback("Paint",click)
colour=(0,0,0)
line_width=3
radius=100
pre_point=(None,None)
text=input("Enter text to write\n")
if text:
	cap=cv2.VideoCapture(0)
	while True:
		ret,frame=cap.read()
		# frame=cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(frame,text,pre_point, font, 2,colour,2,cv2.LINE_AA)
			
		# cv2.circle(frame,pre_point,radius,colour,line_width)
		cv2.imshow("Paint",frame)
		ch=cv2.waitKey(1) #every 1 milli second
		if ch&0xFF==ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()
