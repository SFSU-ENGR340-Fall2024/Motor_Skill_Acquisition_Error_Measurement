import cv2
from tkinter import simpledialog, messagebox
import tkinter as tk
import numpy as np

# Initialize Tkinter root (needed for simpledialog)
root = tk.Tk()
root.withdraw()  # Hide the main window

ImageDisplayWidth = 800
ImageDisplayHeight = 600
image_path = r'C:\Users\milto\OneDrive\Desktop\ImagineProcessClass\.venv\data\calimage.JPG'

# Class to process images
class ImageProcess:
    def __init__(self, image, width=800, height=600):
        self.image = image
        self.imageresized = cv2.resize(self.image, (width, height))
        self.original_image = self.imageresized.copy()  # Store a copy of the original image
        self.points = []  # List to store clicked points
        self.measurement = 1  # Assume the points represent 1 meter

    # Method to check where the left mouse button is clicked
    def checkclicks(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:  # Check if left mouse button is clicked
            print("Left mouse button clicked at:", x, y)
            self.drawcircle(x, y)
            self.points.append((x, y))  # Store the coordinates
            print("Points:", self.points)

    # Method to draw a circle on the image
    def drawcircle(self, x, y):
        cv2.circle(self.imageresized, (x, y), 3, (255, 0, 0), 1)
        cv2.imshow('Test Image', self.imageresized)

    # Method to draw a line between two points on the image
    def drawline(self, point1, point2):
        cv2.line(self.imageresized, point1, point2, (0, 255, 0), 1)
        cv2.imshow('Test Image', self.imageresized)

    # Method to collect calibration points from the user
    def measurementcollect(self):
        cv2.namedWindow('Test Image')  # Create the window
        cv2.setMouseCallback('Test Image', self.checkclicks)

        while True:
            cv2.imshow('Test Image', self.imageresized)
            # Exit the loop if two points have been selected
            if len(self.points) >= 2:
                print("Calibration complete with points:", self.points)
                break
            # Wait for a short period to allow for window refresh
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Calibration canceled.")
                break

        cv2.waitKey(1)  
        cv2.destroyAllWindows()  # Close the window

    # Method to reset the image 
    def reset(self):
        self.imageresized = self.original_image.copy()  # Reset to the original image
        print("Image and points reset.")

    # Method to display text in the middle of the image with a gray background
    def displaytextmiddle(self, text):
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        font_color = (255, 255, 255)  # White text
        thickness = 2
        text_size, _ = cv2.getTextSize(text, font, font_scale, thickness)

        # Calculate the position for the text (centered)
        text_x = (self.imageresized.shape[1] - text_size[0]) // 2
        text_y = (self.imageresized.shape[0] + text_size[1]) // 2

        # Draw a gray background rectangle behind the text
        background_color = (128, 128, 128)  # Gray background
        rectangle_top_left = (text_x - 10, text_y - text_size[1] - 10)  # Some padding
        rectangle_bottom_right = (text_x + text_size[0] + 10, text_y + 10)
        cv2.rectangle(self.imageresized, rectangle_top_left, rectangle_bottom_right, background_color, cv2.FILLED)

        # Put the text on the image
        cv2.putText(self.imageresized, text, (text_x, text_y), font, font_scale, font_color, thickness, cv2.LINE_AA)

        # Show the updated image with the text in the middle
        cv2.imshow('Test Image', self.imageresized)

    def calibration(self): 
        # Reset the image to its original state
        self.reset()
        cv2.waitKey(1)  # Optional, but ensures smoothness in some environments

        # Reopen the 'Measurement Collection' window with the reset image
        for point in self.points:
            self.drawcircle(point[0], point[1])

        # Draw a line between the two points
        self.drawline(self.points[0], self.points[1])

        # Prompt the user for the calibration measurement
        real_world_distance = simpledialog.askstring("Input", "Enter your value in meters:")
        
        # Convert the input to a float, handling possible errors
        try:
            real_world_distance = float(real_world_distance)
        except (ValueError, TypeError):
            messagebox.showerror("Input Error", "Invalid input. Please enter a numeric value.")
            real_world_distance = 0  # Default to 0 if input is invalid

        # Calculate the pixel distance between the two points
        pixel_distance = np.sqrt((self.points[1][0] - self.points[0][0]) ** 2 + (self.points[1][1] - self.points[0][1]) ** 2)

        # Calculate the scaling factor (real-world distance per pixel)
        scaling_factor = real_world_distance / pixel_distance if pixel_distance > 0 else 0

        # Prepare the text to display
        scaling_text = f"Scaling factor: {scaling_factor:.2f} meters/pixel"

        # Reset the image and draw points and lines again
        self.reset()
        cv2.waitKey(1)  # Optional, but ensures smoothness in some environments
        for point in self.points:
            self.drawcircle(point[0], point[1])
        self.drawline(self.points[0], self.points[1])

        # Display the result texts
        self.displaytextmiddle(f"Each Pixel is {scaling_text}")

        cv2.waitKey(10000)  # Wait 10 seconds before proceeding
        cv2.destroyAllWindows()  # Close the window
        


# Load an image
image = cv2.imread(image_path)
img_process = ImageProcess(image, ImageDisplayWidth, ImageDisplayHeight)
# Collect points for calibration
img_process.measurementcollect()
# Calibrate the system
img_process.calibration()
