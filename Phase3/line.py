import cv2

image = cv2.imread('Phase3\\taskimg.webp')

if image is not None:
    pt1 = (50, 100) # 50 col & 100 row
    pt2 = (500, 300) # 500 col & 300 row.

    color = (0, 255, 0)
    thickness = 3

    cv2.line(image, pt1, pt2, color, thickness)
    cv2.imshow('Image with Line', image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()