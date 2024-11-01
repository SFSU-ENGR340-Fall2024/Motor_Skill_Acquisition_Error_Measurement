import sys, os
import cv2
from tkinter import simpledialog, messagebox
import tkinter as tk
import numpy as np


class classtest():
    def __init__(self):
        self.image = None
        self.points = []

    ############################################################################################################
    # Method for the image processing
    ############################################################################################################

    # Method to draw a circle on the image given the x and y coordinates and the image
    # Input: x, y {integers} - the x and y coordinates of the point
    # Output: Redrawn image with the circle drawn
    def drawcircle(self, x, y, image):
        cv2.circle(image, (x, y), 3, (255, 0, 0), 1)
        cv2.imshow('Test Image', image)


    # Method to check where the left mouse button is clicked
    # Input: event, x, y, flags, param
    # Output: x, y position of the mouse click
    def checkclicks(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:  # Check if left mouse button is clicked
            print("Left mouse button clicked at:", x, y)
            self.drawcircle(x, y,self.image)
            self.points.append((x, y))
        else:
            return None
        
    # Method to draw a line between two points on the image
    # Input: x1, y1, x2, y2 (two points), image
    # Output: Redrawn image with the line drawn
    def drawline(self, x1, y1, x2, y2, image):
        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 1)
        cv2.imshow('Test Image', image)

    # Method to clear the image by reloading the original image
    # Input: image, original_image
    # Output: none
    def restartimage(self, image, original_image):
        cv2.destroyAllWindows()
        cv2.waitKey(1)
        image = original_image

    # Method to display text at the bottom of the image with a transparent background
    # Input: image, text
    # Output: image with text displayed
    def displaytextrightbottom(self, image, text):
        font = cv2.FONT_HERSHEY_PLAIN
        font_scale = 1.5
        font_color = (255, 0, 0)  # Blue text
        thickness = 1
        background_color = (200, 200, 200)  # Light gray color
        transparency = 0.5  # Adjust the transparency level (0 = fully transparent, 1 = fully opaque)

        # Split the text into lines
        lines = text.split('\n')

        # Calculate the initial position for the first line
        text_x = image.shape[1] - cv2.getTextSize(lines[0], font, font_scale, thickness)[0][0] - 10  # Align to the right with 10 pixels padding
        start_y = image.shape[0] - 10  # 10 pixels from the bottom

        # Calculate the height of the background rectangle
        total_height = sum(cv2.getTextSize(line, font, font_scale, thickness)[0][1] + 5 for line in lines) + 10  # Adding 10 pixels for padding

        # Create a transparent overlay for the background
        overlay = image.copy()
        cv2.rectangle(overlay, (text_x - 10, start_y - total_height), (image.shape[1], start_y + 10), background_color, -1)  # Background rectangle

        # Blend the overlay with the original image
        cv2.addWeighted(overlay, transparency, image, 1 - transparency, 0, image)

        # Put each line of text on the image
        for i, line in enumerate(lines):
            # Calculate the vertical position for each line
            text_y = start_y - (i * (cv2.getTextSize(line, font, font_scale, thickness)[0][1] + 5))  # Adding 5 pixels spacing
            cv2.putText(image, line, (text_x, text_y), font, font_scale, font_color, thickness, cv2.LINE_AA)

        # Show the updated image with the text at the bottom
        cv2.imshow('Test Image', image)

    # Method to display text at the middle of the image with a background
    # Input: image, text
    # Output: image with text displayed

    def displaytextcenter(self, image, text):
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        font_color = (255, 255, 255)  # White text
        thickness = 2
        text_size, _ = cv2.getTextSize(text, font, font_scale, thickness)

        # Calculate the position for the text (centered)
        text_x = (image.shape[1] - text_size[0]) // 2
        text_y = (image.shape[0] + text_size[1]) // 2

        # Draw a gray background rectangle behind the text
        background_color = (128, 128, 128)  # Gray background
        rectangle_top_left = (text_x - 10, text_y - text_size[1] - 10)  # Some padding
        rectangle_bottom_right = (text_x + text_size[0] + 10, text_y + 10)
        cv2.rectangle(image, rectangle_top_left, rectangle_bottom_right, background_color, cv2.FILLED)

        # Put the text on the image
        cv2.putText(image, text, (text_x, text_y), font, font_scale, font_color, thickness, cv2.LINE_AA)

        # Show the updated image with the text in the middle
        cv2.imshow('Test Image', image)

    # Method to collect the x and y coordinates of the two point for the calibration 
    # Input: image
    # Output: x1, y1, x2, y2

    def calibration_point_collection(self, image):
        self.points = []
        self.image = image
        cv2.namedWindow('Calibration Window')  # Create the window
        cv2.setMouseCallback('Calibration Window', self.checkclicks)
        # Set the mouse callback function
        while True:
            cv2.imshow('Calibration Window', self.image)  # Display the image
            # Exit the loop if two points have been selected
            if len(object.get_points()) >= 2:
                print("Calibration complete with points:", image)
                break
            # Wait for a short period to allow for window refresh
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Calibration canceled.")
                break
        cv2.waitKey(1)  
        cv2.destroyAllWindows()  # Close the window

    def testimage(self, image):
        cv2.imshow('Test Image', image)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()

    def create_window(self, image):
        cv2.namedWindow('Window for calibration')
        cv2.imshow('Window for calibration', image)

        
