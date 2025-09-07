import cv2

image = cv2.imread('Phase5\green_tree.webp')

blurred_image = cv2.medianBlur(image, 5)

cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()