# THRESH_BINARY will set pixel values to maxVal (255) if they are above the threshold value (130), otherwise to 0.
import cv2
# Threashold is applied only on grayscale image
image = cv2.imread('Phase6\\elephant.webp', cv2.IMREAD_GRAYSCALE)

ret , thresh_img = cv2.threshold(image, 130, 255, cv2.THRESH_BINARY)

cv2.imshow('Original Image', image)
cv2.imshow('Thresholded Image', thresh_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


"""
0-90 -- black
91-255 -- white
"""