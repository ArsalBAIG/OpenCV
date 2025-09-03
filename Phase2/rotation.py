import cv2

image = cv2.imread('Phase2\\taskimg.webp')

if image is None:
    print('Image not found')
else:
    (h, w) = image.shape[:2]
    centre = (w// 2, h// 2)
    matrix = cv2.getRotationMatrix2D(center= centre, angle= 90, scale= 1.0)
    roated_img = cv2.warpAffine(image, matrix, (w, h))

    cv2.imshow('Original Image', image)
    cv2.imshow('Rotated Image', roated_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()