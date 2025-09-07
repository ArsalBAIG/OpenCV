import cv2

image = cv2.imread('Phase7\\triangle img.webp')
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, threshold = cv2.threshold(gray_img, 150, 255, cv2.THRESH_BINARY_INV)
contours , hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

for contour in contours:
    area = cv2.contourArea(contour)
    if area > 500:
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
        corners = len(approx)

        if corners == 3:
            shape_name = "Triangle"
        elif corners == 4:
            shape_name = 'Rectangle'
        elif corners == 5:
            shape_name = 'Pentagon'
        elif corners == 6:
            shape_name = 'Hexagon'
        elif corners > 6:
            shape_name = 'Circle'
        else:
            shape_name = 'Unknown!'

        cv2.drawContours(image, [approx], -1, (0, 0, 255), 2)
    
        x = approx.ravel()[0]
        y = approx.ravel()[1] - 10 # move the text label slightly above the shape's corner.
        cv2.putText(image, shape_name, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()