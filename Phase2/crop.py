import cv2

image = cv2.imread('Phase2\\taskimg.webp')

if image is not None: # 100: 200 rep rows(y-axis) and vise-versa.
    cropped = image[100:200, 50: 150]
    cv2.imshow('Original Image', image)
    cv2.imshow('Cropped Image', cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()