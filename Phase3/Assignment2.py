import cv2
import ast

img_path = input('Give me your file location: ')
image = cv2.imread(img_path)

if image is None:
    print("Error loading Image!")
    exit()

user_inp = input('Whether you want to draw <line, rectangle, circle, text?> ')

if user_inp.lower() == 'line':
    coords = input('Tell the coordinates of lines ((x1,y1),(x2,y2)): ')
    pt1, pt2 = ast.literal_eval(coords)
    cv2.line(image, pt1, pt2, (0, 255, 0), 3)
    user_inp = input('Do you want to save image? (yes/no)?')
    
    if user_inp.lower() == 'yes':
        cv2.imwrite('final_image.png', image)
    else:
        pass

elif user_inp.lower() == 'rectangle':
    coords = input('Tell the coordinates of pt1, pt2 ((x1,y1),(x2,y2)): ')
    pt1, pt2 = ast.literal_eval(coords)
    cv2.rectangle(image, pt1, pt2, (0, 0, 255), 3)

    user_inp = input('Do you want to save image? (yes/no)?')
    if user_inp.lower() == 'yes':
        cv2.imwrite('final_image.png', image)
    else:
        pass

elif user_inp.lower() == 'circle':
    coords = input('Tell the coordinates like ((x,y), radius): ')
    centre, radius = ast.literal_eval(coords)
    cv2.circle(image, centre, radius, (255, 0, 0), 3)

    user_inp = input('Do you want to save image? (yes/no)?')
    if user_inp.lower() == 'yes':
        cv2.imwrite('final_image.png', image)
    else:
        pass

else:  
    coords = input('Enter text and coordinates like ("Hello", (x,y)): ')
    text, org = ast.literal_eval(coords)
    cv2.putText(image, text, org, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    user_inp = input('Do you want to save image? (yes/no)?')
    if user_inp.lower() == 'yes':
        cv2.imwrite('final_image.png', image)
    else:
        pass

cv2.imshow('Result', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
