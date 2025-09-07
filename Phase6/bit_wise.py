# Note: Image1,2 should be of same size and type.
# Note: Use gray scale or black-white images
import cv2
import numpy as np

image1 = np.zeros((250, 250), dtype="uint8")
image2 = np.zeros((250, 250), dtype="uint8")

img1 = cv2.circle(image1, (120, 120), 50, 255, 2)
img2 = cv2.rectangle(image2, (120, 120), (180, 180), 255, 2)

bitwise_and = cv2.bitwise_and(img1, img2)
bitwise_or = cv2.bitwise_or(img1, img2)
bitwise_not = cv2.bitwise_not(img2)

cv2.imshow('Image 1', img1)
cv2.imshow('Image 2', img2)
cv2.imshow('Bitwise AND', bitwise_and)
cv2.imshow('Bitwise OR', bitwise_or)
cv2.imshow('Bitwise NOT', bitwise_not)

cv2.waitKey(0)
cv2.destroyAllWindows()