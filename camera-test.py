import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    # Capture frame by frame
    ret, frame = cap.read()

    # Display the resulting frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', frame)
    cv2.imshow('frame1', gray)
    cv2.imshow('frame2', frame)
    cv2.imshow('frame3', frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
