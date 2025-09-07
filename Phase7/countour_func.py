# Countours is the process of finding edges.
import cv2

image = cv2.imread('Phase7\\triangle img.webp')
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# '_' is used to ignore the first return value.
_, threshold = cv2.threshold(gray_img, 150, 255, cv2.THRESH_BINARY)

# 'cv2.RETR_TREE' retrieves all contours and reconstructs a full hierarchy of family contours.

# 'cv2.CHAIN_APPROX_SIMPLE' compresses horizontal, vertical, and diagonal segments
contours, hierarchy = cv2.findContours(gray_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# -1 indicates all contours to be drawn.
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows() 