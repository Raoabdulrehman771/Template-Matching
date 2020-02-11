import cv2
import numpy as np
from playsound import playsound

scale_percent = 50
template = cv2.imread('pic8.jpg',0)
width1 = int(template.shape[1] * scale_percent / 100)
height1 = int(template.shape[0] * scale_percent / 100)
dim1 = (width1, height1)
# resize image
resized2 = cv2.resize(template, dim1, interpolation = cv2.INTER_AREA)

face_w, face_h = resized2.shape[::-1]

cv2.namedWindow('image') 

cap = cv2.VideoCapture(1)

threshold = 0.8
ret = True
count = 1

while ret :
	count = 1
	ret, img = cap.read()
	#if count == 1:         #First you have run these two lines for capturing the frist frame then terminate the code select the object which you want to match in real time and save the jpg image and comments these two lines again and run the code.
	#	cv2.imwrite("pic8.jpg",img)
	width = int(img.shape[1] * scale_percent / 100)
	height = int(img.shape[0] * scale_percent / 100)
	dim = (width, height)
	# resize image
	resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
	
	img_gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
	res = cv2.matchTemplate(img_gray,resized2,cv2.TM_CCOEFF_NORMED)
	if len(res):
		location = np.where( res >= threshold)
		for pt in zip(*location[::-1]):
            #puting  rectangle on recognized erea 
			cv2.rectangle(resized, pt, (pt[0] + face_w, pt[1] + face_h), (0,0,255), 2)
			count = 0
	if count == 1:
		print("Nooooooo......!!!!")
		playsound("alert.mp3")
	
	cv2.imshow('image',resized)
	key = cv2.waitKey(1) & 0xFF
	if key == ord('q'):
		break
cv2.destroyAllWindows()
