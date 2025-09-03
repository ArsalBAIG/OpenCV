import cv2

image = cv2.imread('Phase3\\taskimg.webp')

if image is not None:
    cv2.putText(image, 'OpenCV', (40, 25), fontFace= cv2.FONT_ITALIC, fontScale= 1, thickness= 2, color= (0, 255, 0))
    cv2.imshow('Image with Text', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()