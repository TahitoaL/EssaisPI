import numpy as np
import cv2


video = cv2.VideoCapture("test2.mp4")
if video.isOpened():
	while True:
		check, frame = video.read()

		frame = cv2.GaussianBlur(frame,(5,5),0)

		# frame = cv2.gauss
		canny = cv2.Canny(frame, 120, 100)
		# canny2 = cv2.Canny(frame, 500, 100)
		# canny3 = cv2.Canny(frame, 150, 300)
		if check:
			cv2.imshow("Frame", frame)
			cv2.imshow("orginal with line", canny)
			# cv2.imshow("orginal with line2", canny2)
			# cv2.imshow("orginal with line3", canny3)
			key = cv2.waitKey(50)
			if key == ord('q'):
				break
		else:
			print('Frame not available')
			print(video.isOpened())