# Python program to illustrate 
# template matching 

from imutils.video import VideoStream
from imutils.video import FPS
import imutils
import time
import cv2 
import numpy as np

# Read the main image 
cap = cv2.VideoCapture(0) #Webcam Capture
template = cv2.imread('pic6.jpg',0)

while(True):

	ret, frame = cap.read()
	#img_rgb = cv2.imread('pic3.jpg') 
	
	scale_percent = 50 # percent of original size
	width = int(frame.shape[1] * scale_percent / 100)
	height = int(frame.shape[0] * scale_percent / 100)
	dim = (width, height)
	# resize image
	resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
	#print('Resized Dimensions : ',resized.shape)
	
	# Convert it to grayscale 
	img_gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY) 

	# Read the template 
	template = cv2.imread('pic5.jpg',0) 

	scale_percent = 50 # percent of original size
	width = int(template.shape[1] * scale_percent / 100)
	height = int(template.shape[0] * scale_percent / 100)
	dim = (width, height)
	# resize image
	resized2 = cv2.resize(template, dim, interpolation = cv2.INTER_AREA)
	
	# Store width and height of template in w and h 
	w, h = resized2.shape[::-1] 

	# Perform match operations. 
	res = cv2.matchTemplate(img_gray,resized2,cv2.TM_CCOEFF_NORMED) 

	# Specify a threshold 
	threshold = 0.8
	
	# Store the coordinates of matched area in a numpy array 
	loc = np.where( res >= threshold) 
	
	# Draw a rectangle around the matched region. 
	for pt in zip(*loc[::-1]): 
		cv2.rectangle(resized, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2) 

	# Show the final image with the matched area. 
	#cv2.imshow('Detected',resized)
	
	cv2.imshow("Frame", frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cv2.destroyAllWindows()	