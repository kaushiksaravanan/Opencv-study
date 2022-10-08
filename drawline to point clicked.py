#open cam draw line from 0,0 to the point clicked

import cv2
cap=cv2.VideoCapture(0)


def click(event,x,y,flags,param):
	global pre_point,fin_point,pressed
	if event==cv2.EVENT_LBUTTONDOWN:
		# print('pressed',x,y,radius)
		pre_point=(x,y)
		fin_point=(0 ,0)
		# print(pre_point,fin_point)
#

cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame",click)
colour=(0,255,0)
line_width=3
radius=100
pre_point=(None,None)
fin_point=(None,None)
while True:
	ret,frame=cap.read()
	# frame=cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
	# cv2.circle(frame,point,radius,colour,line_width)
	cv2.line(frame,pre_point,fin_point,colour,line_width)
	cv2.imshow("Frame",frame)
	ch=cv2.waitKey(1) #every 1 milli second
	if ch&0xFF==ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
