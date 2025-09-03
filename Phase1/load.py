import cv2

image = cv2.imread('Python-01.webp')

if image is None:
    print("Error: Could not load image.")
else:
    print('Image loaded successfully.')