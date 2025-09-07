import cv2

camera = cv2.VideoCapture(0)

frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
# codec is use for compression and decompression of video.

codec = cv2.VideoWriter_fourcc(*'XVID') # fourcc rep four-char-code.
recorded = cv2.VideoWriter('My Video.avi', codec, 30.0, (frame_width, frame_height))

while True:
    success, image = camera.read()

    if not success:
        print('Failed to capture video frame')
        break
    recorded.write(image)
    cv2.imshow('Video Frame', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print('Quitting!')
        break

camera.release()
recorded.release()