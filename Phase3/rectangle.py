import cv2

image = cv2.imread('Phase3\\taskimg.webp')

if image is not None:
    pt1 = (50, 100)
    pt2 = (500, 300)

    cv2.rectangle(image, pt1, pt2, (0, 0, 255), 3)
    cv2.imshow('Image with Rectangle', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()