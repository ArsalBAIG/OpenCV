import cv2
import numpy as np

image = cv2.imread('Phase5\low_res.webp')

sharpen_array = np.array([
    [0, -1, 0],
    [-1, 5,-1],
    [0, -1, 0]
])

sharpen = cv2.filter2D(image, -1, sharpen_array)

cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpen)
cv2.waitKey(0)
cv2.destroyAllWindows()