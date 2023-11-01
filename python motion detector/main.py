import cv2
cam = cv2.VideoCapture(0)
while cam.isOpened():
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
    diff = cv2.absdiff(frame1, frame2)
    _, thresh = cv2. threshold(diff, 25, 255, cv2.THRESH_BINARY)
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow('Oten Detector', diff)
