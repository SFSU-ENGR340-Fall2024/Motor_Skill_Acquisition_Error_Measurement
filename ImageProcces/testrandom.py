import cv2
import tkinter as tk
from tkinter import simpledialog

ImageDisplayWidth = 800
ImageDisplayHeight = 600
image_path = r'C:\Users\milto\OneDrive\Desktop\ImagineProcessClass\.venv\data\calimage.JPG'

# Class to process images
class ImageProcess:
    def __init__(self, image, width=800, height=600):
        self.image = image
        self.imageresized = cv2.resize(self.image, (width, height))
        self.input_text = ""  # Variable to store user input

    # Method to display the image with input text
    def display_image(self):
        # Create a copy of the resized image to draw on
        image_with_text = self.imageresized.copy()
        input_box_height = 50  # Height of the input box
        # Draw the input box
        cv2.rectangle(image_with_text, 
                      (10, image_with_text.shape[0] - input_box_height - 10), 
                      (image_with_text.shape[1] - 10, image_with_text.shape[0] - 10), 
                      (255, 255, 255), -1)  # White box for input
        # Put the input text on the image
        cv2.putText(image_with_text, self.input_text, 
                    (15, image_with_text.shape[0] - 15), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)  # Black text
        cv2.imshow('Input Box', image_with_text)

    # Method to get user input using Tkinter dialog
    def get_user_input(self):
        # Create a simple dialog to get user input
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        self.input_text = simpledialog.askstring("Input", "Please enter your text:")
        root.destroy()  # Close the dialog

        # Display the input text on the image
        self.display_image()
        print("User Input:", self.input_text)

# Load an image
image = cv2.imread(image_path)

if image is not None:  # Ensure the image loaded successfully
    # Create an instance of the ImageProcess class
    img_process = ImageProcess(image, ImageDisplayWidth, ImageDisplayHeight)
    # Get user input
    img_process.get_user_input()
    cv2.waitKey(0)  # Wait indefinitely until a key is pressed
    cv2.destroyAllWindows()  # Close the window
else:
    print("Error: Image could not be loaded. Please check the file path.")
