import cv2

image = cv2.imread('Python-01.webp')

if image is not None:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('GrayScale Image', gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Image not found or unable to load.")