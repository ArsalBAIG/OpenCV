import cv2

image = cv2.imread('Phase3\\taskimg.webp')

if image is not None:
    centre = (280, 150)
    radius = 100

    cv2.circle(image, centre, radius, (255, 0, 0), 3)
    cv2.imshow('Image with Circle', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()