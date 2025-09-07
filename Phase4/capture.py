import cv2
# 0 for in-built webcam & 1 for external webcam.
capture = cv2.VideoCapture(0) 

while True:
    ret, frame = capture.read() # ret = return where ret is T/F.

    if not ret:
        print('Failed to capture frame')
        break
    cv2.imshow('Video Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): # This code will fetch ASCII num.
        print('Quitting!') # when 'q' is pressed the loop will break/exist.
        break
capture.release()
cv2.destroyAllWindows()