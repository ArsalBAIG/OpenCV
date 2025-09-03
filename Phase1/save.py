import cv2

image = cv2.imread('Python-01.webp')

if image is not None:
    final = cv2.imwrite('Python-01_copy.webp', image)
    
    if final:
        print('Image saved successfully to Python-01_copy.webp.')
    else:
        print('Error: Could not save image.')
else:
    print('Error: Failed to load the original image.')