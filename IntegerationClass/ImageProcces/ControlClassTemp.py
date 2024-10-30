from ImageProcces import ImageProcess
from DataClassTemp import DataClass
from GUICopy import GUI

import cv2

ImageDisplayWidth = 1500
ImageDisplayHeight = 700
image_path = r'Motor_Skill_Acquisition_Error_Measurement\IntegerationClass\ImageProcces\RulerPicture.jpg'





def load_and_display_image(image_path, width, height):
    # Load the image
    image = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if image is None:
        print(f"Error: Image not found or could not be loaded from: {image_path}")
        return
    
    # Print the shape of the loaded image
    print("Loaded image shape:", image.shape)

    # Resize the image
    resized_image = cv2.resize(image, (width, height))

    # Show the resized image in a window
    cv2.imshow('Test Image', resized_image)
    cv2.waitKey(0)  # Wait until a key is pressed
    cv2.destroyAllWindows()  # Close the window

def main():
    image_path = 'path/to/your/image.jpg'  # Replace with your image path
    width, height = 640, 480  # Desired dimensions for resizing
    load_and_display_image(image_path, width, height)

if __name__ == "__main__":
    main()
