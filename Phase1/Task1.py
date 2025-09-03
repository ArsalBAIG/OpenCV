import cv2

IMAGE_PATH = 'Phase1\\taskimg.webp'
img_loc = input('Enter the image location?')


img = cv2.imread('Phase1\\taskimg.webp')

if img is None:
    print(f"Error: Could not read the image from {IMAGE_PATH}.")
else:
    user_input = input('Do you want to show the image or save it?')

    if user_input.lower() == 'show':
        cv2.imshow('Image Display', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print('Image Displayed Successfully.')

    elif user_input.lower() == 'save':
        user_file_name = input('Enter the name you want to save the file as (e.g., my_image.webp): ')
        save_path = f'Phase1\\{user_file_name}'
        cv2.imwrite(save_path, img)
    else:
        print("Invalid input. Please enter 'show' or 'save'.")