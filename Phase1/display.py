import cv2

image = cv2.imread('Python-01.webp')

if image is not None:
    cv2.imshow('Image', image)
    cv2.waitKey(0) # opens the image until no key is pressed.
    cv2.destroyAllWindows() # closes all OpenCV windows.
else:
    print('Error: Could not display image.')