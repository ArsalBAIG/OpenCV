import cv2

image = cv2.imread('Phase5\green_tree.webp')

# GaussianBlur will works by taking the average of the pixels around the target pixel.
blurred_image = cv2.GaussianBlur(image, (5, 5), 0) # 0 reps that cv2 will handle it own it own.

cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()