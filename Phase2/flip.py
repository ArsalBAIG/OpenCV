import cv2

image = cv2.imread('Phase2\\taskimg.webp')

if image is not None:
    flipped_hor = cv2.flip(image, 1) # 0 for vertical and -1 for both
    flipped_ver = cv2.flip(image, -0)
    flipped_both = cv2.flip(image, -1)

    cv2.imshow('Original Image', image)
    cv2.imshow('Flipped Horizontal', flipped_hor)
    cv2.imshow('Flipped Vertical', flipped_ver)
    cv2.imshow('Flipped Both', flipped_both)

    cv2.waitKey(0)
    cv2.destroyAllWindows()