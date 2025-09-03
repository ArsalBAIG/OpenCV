import cv2

image = cv2.imread('Phase2\\taskimg.webp')

if image is None:
    print('Image not found')
else:
    print('Image found') # first width then height
    resized_image = cv2.resize(image, (300, 300))

    cv2.imshow('Original Image', image)
    cv2.imshow('Resized Image', resized_image)

    cv2.imwrite('Resize_Image.png', resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()