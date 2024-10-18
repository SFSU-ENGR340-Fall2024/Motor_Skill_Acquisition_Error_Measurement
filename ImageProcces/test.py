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
nextimage = r'C:\Users\milto\OneDrive\Desktop\ImagineProcessClass\.venv\data\IMG_1687.JPG'

# Class to process images
class ImageProcess:
    def __init__(self, image, width=800, height=600):
        self.image = image
        self.imageresized = cv2.resize(self.image, (width, height))
        self.original_image = self.imageresized.copy()  # Store a copy of the original image
        self.nextimage = nextimage
        self.points = []  # List to store clicked points
        self.measurement = 1  # Assume the points represent 1 meter
        self.center = []
        self.puck = []
        self.error_measurement_value = None  # Changed here
        self.errorXY = []
        self.errorImage = None
        self.scaling_factor = None
    
    # Update image to next image 
    def updateImage(self, width=800, height=600):
        self.imageresized = cv2.resize(cv2.imread(self.nextimage), (width, height))
        self.original_image = self.imageresized.copy() 

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
        self.points.clear()  # Clear any stored points
        print("Image and points reset.")

    # Method to display text at the bottom of the image without a background
    def displaytextbottom(self, text):
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        font_color = (255, 255, 255)  # White text
        thickness = 2
        text_size, _ = cv2.getTextSize(text, font, font_scale, thickness)

        # Calculate the position for the text at the bottom of the image
        text_x = (self.imageresized.shape[1] - text_size[0]) // 2  # Center horizontally
        text_y = self.imageresized.shape[0] - 10  # 10 pixels from the bottom

        # Put the text on the image
        cv2.putText(self.imageresized, text, (text_x, text_y), font, font_scale, font_color, thickness, cv2.LINE_AA)

        # Show the updated image with the text at the bottom
        cv2.imshow('Test Image', self.imageresized)

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
        # Check if enough points have been collected
        if len(self.points) < 2:
            print("Not enough points collected for calibration.")
            return

        # Reset the image to its original state without clearing points
        self.imageresized = self.original_image.copy()  # Reset to the original image
        print("Image reset, points retained.")

        # Draw the collected points
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
            return  # Exit the method if input is invalid

        # Calculate the pixel distance between the two points
        pixel_distance = np.sqrt((self.points[1][0] - self.points[0][0]) ** 2 + (self.points[1][1] - self.points[0][1]) ** 2)

        # Calculate the scaling factor (real-world distance per pixel)
        self.scaling_factor = real_world_distance / pixel_distance if pixel_distance > 0 else 0

        # Prepare the text to display
        scaling_text = f"Scaling factor: {self.scaling_factor:.2f} meters/pixel"

        # Reset the image to display results without losing original image
        self.imageresized = self.original_image.copy()  # Reset to the original image

        # Draw the points and the line again
        for point in self.points:
            self.drawcircle(point[0], point[1])
        self.drawline(self.points[0], self.points[1])

        # Display the result texts
        self.displaytextmiddle(f"Each Pixel is {scaling_text}")

        cv2.waitKey(10000)  # Wait 10 seconds before proceeding
        cv2.destroyAllWindows()  # Close the window
    
        

    def errormeasurment(self):
        self.reset()
        cv2.waitKey(1)  # Optional, but ensures smoothness in some environments
        cv2.namedWindow('Test Image')  # Create the window
        
        # Collect the center point
        cv2.setMouseCallback('Test Image', self.checkcenter)
        self.displaytextmiddle("Please click on the center")

        while True:
            cv2.imshow('Test Image', self.imageresized)
            if self.center:  # Check if center point is captured
                print("Calibration complete with center point:", self.center)
                break
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Calibration canceled.")
                break

        cv2.waitKey(1)  

        # Collect puck point
        self.points.clear()  # Clear previous points
        cv2.setMouseCallback('Test Image', self.checkpuck)
        self.displaytextmiddle("Please click on the puck")

        while True:
            cv2.imshow('Test Image', self.imageresized)
            if self.puck:  # Check if puck point is captured
                print("Calibration complete with puck point:", self.puck)
                break
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Calibration canceled.")
                break

        cv2.waitKey(1)  
        self.calculate_error()  # Call the method to calculate and display error

    def checkcenter(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:  # Check if left mouse button is clicked
            print("Center clicked at:", x, y)
            self.center = (x, y)  # Store the center point
            self.drawcircle(x, y)  # Draw a circle at the clicked position
            cv2.imshow('Test Image', self.imageresized)

    def checkpuck(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:  # Check if left mouse button is clicked
            print("Puck clicked at:", x, y)
            self.puck = (x, y)  # Store the puck point
            self.drawcircle(x, y)  # Draw a circle at the clicked position
            cv2.imshow('Test Image', self.imageresized)

    def calculate_error(self):
        if self.center and self.puck:
            # Calculate the difference in coordinates
            diff_x = self.puck[0] - self.center[0]
            diff_y = self.puck[1] - self.center[1]

            # Calculate the Euclidean distance
            error_distance = np.sqrt(diff_x**2 + diff_y**2)

            # Prepare the error message
            error_message = f"Error: {(error_distance * self.scaling_factor):.2f} meters"  # If you want it in meters
            print(error_message)

            # Display the error message
            self.displaytextmiddle(error_message)

            # Wait for a moment before proceeding
            cv2.waitKey(5000)  # Wait 5 seconds
        else:
            print("Error calculation skipped: Center or puck not defined.")

# Load and process the image
image = cv2.imread(image_path)
processor = ImageProcess(image)

# Collect calibration points
processor.measurementcollect()
processor.calibration()
processor.errormeasurment()

# Clean up and exit
cv2.destroyAllWindows()
