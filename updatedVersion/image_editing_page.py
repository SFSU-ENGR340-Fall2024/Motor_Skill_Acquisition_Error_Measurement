
############################################################################################
# Project Name: Motor Skill Acquisition Error Management System (San Francisco State University Project 2024) 
# 
# Filename: image_editing_page.py
# 
# Authors: Milton Tinoco, Ethan Weldon, Joshua Samson, Michael Cabrera
#
# Last Update: 12/08/2024
#
# File Description:
# This file contains the code for the image editing page, where users can select points on images
# to calculate real-world measurements. The EditPage class allows users to select a center point
# and a puck point on the image to calculate the z-axis, y-axis, and x-axis values. The calculated
# values are displayed on the screen and saved to a text file. The page also provides navigation
# options to move between images and return to the main menu. At the end of the image list, users
# can choose to go to the data review page, return to the main menu, or exit the program.
#
############################################################################################

# Import necessary libraries

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt, QTimer
from calculation_class import CalculationsManager
from file_manger_class import FileManager
from image_interface import ImageView
import os
from calibration_page import CalibrationPage
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout


class EditPage(QWidget):
    """
    Description: This class represents the image editing page where users can select points on images to calculate
                 real-world measurements. The EditPage class allows users to select a center point and a puck point
                 on the image to calculate the z-axis, y-axis, and x-axis values. The calculated values are displayed
                 on the screen and saved to a text file. The page also provides navigation options to move between images
                 and return to the main menu. At the end of the image list, users can choose to go to the data review page,
                 return to the main menu, or exit the program.
    """
    def __init__(self, parent): 
        super().__init__()
        self.parent = parent # Save the reference to the parent

        # Initialize the file manager and calculations manager objects
        self.file_manager = FileManager()
        self.calculations_manager = CalculationsManager()

        # Initialize the class attributes

        self.folder_path = None  # Store the selected folder path
        self.image_path = None  # Store the selected image path
        self.axis_orientation = None  # Store the selected axis
        self.scaling_factor = None # Store the scaling factor
        self.image_list = []  # List to store the image paths in the selected folder
        self.image_index = 1 # Index of the current image being displayed
        self.center_point = None  # Store the center point of the image
        self.clicked_points = []  # List to store the clicked points on the image
        self.result_file_path = None # Store the path to the result file
        self.result_folder_path = None # Store the path to the result folder
        self.information_file_path = None # Store the path to the information file
        self.track_clicks = 0  # Number of clicks to track
        self.radial = None # Store the calculated z-axis value
        self.yaxis = None # Store the calculated y-axis value
        self.xaxis = None # Store the calculated x-axis value
        self.layout = QVBoxLayout() # Create a vertical layout for the page

        # Direction label 

        # Create text on the top of the page of directions for the user
        self.direction_label = QLabel("Direction: Click to select the center point")
        # Set the alignment of the text to center
        self.direction_label.setAlignment(Qt.AlignCenter)
        # Set the font size, weight, and margin for the text
        self.direction_label.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 20px;")
        # Add the text to the layout
        self.layout.addWidget(self.direction_label)

        # create a horizontal layout for button

        axis_button_layout = QHBoxLayout()

        # Button to reselect the center point
        # Description: This button allows the user to reselect the center point on the image.
        self.center_button = QPushButton("Reselect Center")
        self.center_button.setEnabled(False)
        self.center_button.clicked.connect(self.reselect_center)
        self.center_button.hide()

        # Button to go back to the previous image
        # Description: This button allows the user to go back to the previous image in the list.
        self.previous_button = QPushButton("Previous Image")
        self.previous_button.clicked.connect(self.previous_image)

        # Button to skip "X" image
        # Description: If image for trial dne, user uses this to add false value to data point
        self.skip_button = QPushButton("No Trial")
        self.skip_button.clicked.connect(self.no_image)

        # Button to skip invalid image
        # Description: If puck is out of the grid's bounds, user clicks this to add outlier value to data
        self.outlier_button = QPushButton("Out of bounds")
        self.outlier_button.clicked.connect(self.invalid_trial)

        # Add buttons to horizontal layout
        buttons = [self.previous_button, self.center_button, self.skip_button, self.outlier_button]
        [axis_button_layout.addWidget(button) for button in buttons]
        [button.setStyleSheet('font-size: 16px') for button in buttons]

        # Add the horizontal layout to the main vertical layout
        self.layout.addLayout(axis_button_layout)

        # Info Label

        # Create text on top of image to display the information
        self.info_label = QLabel(f"First Image:   | Radial: {self.radial} | X-axis: {self.xaxis} | Y-axis: {self.yaxis}")
        # Set the alignment of the text to center
        self.info_label.setAlignment(Qt.AlignCenter)
        # Set the font size, weight, and margin for the text
        self.info_label.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 20px;")
        # Add the text to the layout
        self.layout.addWidget(self.info_label)

        # Image viewer
        # Create an image viewer widget
        self.image_viewer = ImageView()
        # Set the image viewer to track two clicks
        self.image_viewer.track_clicks = self.track_clicks
        # Add the image viewer to the layout
        self.layout.addWidget(self.image_viewer)
        self.setLayout(self.layout)

        # Connect the point_clicked signal from the ImageView to the point_clicked method
        self.image_viewer.point_clicked.connect(self.handle_point_clicked)



    def handle_point_clicked(self, x, y):
        """
        Description: Handle the event when a point is clicked on the image.
                     Append the clicked point to the list of clicked points.
                     Calculate the z-axis, y-axis, and x-axis values based on the selected points.
                     Append the calculated data to the results file.
                     Update the info label with the calculated data.
                     Display the next image after a delay.
        Input: x - x-coordinate of the clicked point
               y - y-coordinate of the clicked point
        Output: None
        """
        # check if the track_clicks is 1 which means that center point is selected
        if self.track_clicks == 1:
            # Append the center point if not already in the list
            if self.center_point and self.center_point not in self.clicked_points:
                self.clicked_points.append(self.center_point)
                self.image_viewer.draw_point_circle(self.center_point[0], self.center_point[1])
            
            # Append the clicked point to the list of clicked points
            self.clicked_points.append((x, y)) 
            # Check if the number of clicked points is 2 to calculate the values
            if len(self.clicked_points) == 2:
                # update the direction label
                self.direction_label.setText("Loading Next Image .....")
                self.image_viewer.track_clicks = self.track_clicks
                self.calulate_and_display() # Calculate the z-axis, y-axis, and x-axis values

        # check if the track_clicks is 2 which means that not selected or reselecting the center point
        else:  
            self.clicked_points.append((x, y)) # Append the clicked point to the list of clicked points

            # Update the direction label for user next step
            if len(self.clicked_points) == 1: 
                self.direction_label.setText("Please click on the puck.")

            # Check if the number of clicked points is 2 to go to the next step to calculate the values
            if len(self.clicked_points) == 2:
                # give update to the user
                self.direction_label.setText("Loading Next Image .....")
                # Set the center point to the first clicked point
                self.center_point = self.clicked_points[0]
                # Set the track_clicks to 1 to and update the next time to only need to click on the puck
                self.track_clicks = 1
                # update the image viewer to track the clicks
                self.image_viewer.track_clicks = self.track_clicks 
                self.calulate_and_display() # Calculate the z-axis, y-axis, and x-axis values
                self.center_button.show() # Show the reselect center button
                self.center_button.setEnabled(True) # Enable the reselect center button

    def calulate_and_display(self):
        """
        Description: Adjust the coordinates based on the user selected axes and center point.
                     Calculate the radial, y-axis, and x-axis values based on the selected points.
                     Append the calculated data to the results file.
                     Update the info label with the calculated data.
    
        Input: None
        Output: None
        """
        # Calculate the offset to make clicked_points[0] the origin
        # Relative x and y values based on the origin point
        origin_x, origin_y = self.clicked_points[0]
        relative_x = self.clicked_points[1][0] - origin_x
        relative_y = self.clicked_points[1][1] - origin_y

        # Determine vertical and horizontal values based on the selected axes
        # Adjust the values based on the selected axis orientation
        # Default orientation is 0 (x-axis: horizontal, y-axis: vertical)

        try:
            if self.axis_orientation == 0: # Default orientation
                vertical_value = relative_x
                horizontal_value = -relative_y

            elif self.axis_orientation == 1: # Custom orientation
                vertical_value = relative_y
                horizontal_value = relative_x

            elif self.axis_orientation == 2: # Custom orientation
                vertical_value = -relative_x
                horizontal_value = relative_y

            elif self.axis_orientation == 3: # Custom orientation
                vertical_value = -relative_y
                horizontal_value = -relative_x

            else:
                raise ValueError("Invalid axis orientation")  # Force an error if out of range

        except ValueError as e:
            print(f"Error: {e}. Resetting to default orientation (0).")
            self.axis_orientation = 0
            vertical_value = relative_x
            horizontal_value = -relative_y


        # Calculate the z-axis error using the adjusted vertical and horizontal values
        self.radial = self.calculations_manager.calculate_error(
            0, 0, vertical_value, horizontal_value, self.scaling_factor
        )

        # If z-axis error is zero, set x and y to zero
        if self.radial == 0:
            self.xaxis = 0
            self.yaxis = 0
        else:
            # Calculate real-world coordinates using the adjusted vertical and horizontal values
            self.xaxis, self.yaxis = self.calculations_manager.calculate_real_world_coordinates(
                0, 0, vertical_value, horizontal_value, self.scaling_factor
            )

        # Append the calculated data to the results file
        self.file_manager.append_axis_data(
            self.result_file_path, self.image_index, self.radial, self.yaxis, self.xaxis
        )

        # Update the info label with the calculated data
        self.info_label.setText(f" On Trial [{self.image_index}] out of [{len(self.image_list) - 1}] || Previous Trial Values: || Radial: {self.radial} | X-axis: {self.xaxis} | Y-axis: {self.yaxis}")
        # Display the next image after a delay
        QTimer.singleShot(500, lambda: self.next_image("Please click on the puck"))

    def reselect_center(self):
        """
        Description: Allow the user to reselect the center point on the image.
                     Reset the track_clicks to 2 and update the image viewer.
                     Load the current image with a message to click on the center again.
        Input: None
        Output: None
        """
        self.track_clicks = 2
        self.image_viewer.track_clicks = self.track_clicks
        self.info_label.setText(f" On Trial [{self.image_index}] out of [{len(self.image_list) - 1}] || Previous Trial Values: || Radial: {self.radial} | X-axis: {self.xaxis} | Y-axis: {self.yaxis}")
        self.load_image(self.image_index, "Please click on the center again to reselect")
       
    def load_image(self,index,text):
        """
        Description: Load the image at the specified index from the image list.
                     Update the direction label with the specified text.
                     Clear the clicked points and load the image in the image viewer.
        Input: index - index of the image to load
               text - text to display in the direction label
        Output: None
        """
        # Validate index
        if index < 0 or index >= len(self.image_list):
            raise IndexError("Index out of range for image list.")
        # Get image path from the list
        image_path = self.image_list[index]
        # Validate image file existence
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image not found: {image_path}")
        # Clear clicked points
        self.image_viewer.click_list = []  # Clear internal clicked points
        self.clicked_points = []  # Clear external clicked points
        # Load the image
        self.image_path = image_path  # Update the current image path
        self.direction_label.setText(text)
        # Load the image in the image viewer
        self.image_viewer.load_image(image_path)  
        # Draw the center point if center point is selected
        if self.track_clicks == 1:
            self.image_viewer.draw_point_circle(self.center_point[0], self.center_point[1])

    def next_image(self, text):
        """
        Description: Load the next image in the image list.
                     Increment the image index and update the information label.
                     Draw the center point on the image viewer.
                     Load the next image with a message to click on the center.
        Input: text - text to display in the direction label
        Output: None
        """
        # Check if the image index is less than the total number of images otherwise the user has reached the end of the images
        if self.image_index < len(self.image_list) - 1: 
            # Increment the image index and update information
            self.image_index += 1 
            self.info_label.setText(f" On Trial [{self.image_index}] out of [{len(self.image_list) - 1}] || Previous Trial Values: || Radial: {self.radial} | X-axis: {self.xaxis} | Y-axis: {self.yaxis}")
            self.image_viewer.draw_point_circle(self.center_point[0], self.center_point[1]) 
            self.load_image(self.image_index, text)

        else:
            # If at the end of the image list, remove image viewer and add options
            QMessageBox.information(self, "End of Images", "All images have been processed.")

            # Add a label to indicate completion
            completion_label = QLabel("Processing complete! What would you like to do next?")
            completion_label.setAlignment(Qt.AlignCenter)
            completion_label.setStyleSheet("font-size: 18px; font-weight: bold;")
            self.layout.addWidget(completion_label)

            # Add a button to navigate to do another trial
            trial_button = QPushButton("Another Trial")
            trial_button.setStyleSheet("font-size: 16px; padding: 10px;")
            trial_button.clicked.connect(self.go_back_to_trial)
            self.layout.addWidget(trial_button)


            # Add a button to navigate to the Data Review Page
            data_review_button = QPushButton("Go to Data Review")
            data_review_button.setStyleSheet("font-size: 16px; padding: 10px;")
            data_review_button.clicked.connect(self.go_to_data_review)
            self.layout.addWidget(data_review_button)

            # Add a button to return to the main menu
            main_menu_button = QPushButton("Back to Main Menu")
            main_menu_button.setStyleSheet("font-size: 16px; padding: 10px;")
            main_menu_button.clicked.connect(self.go_to_main_menu)
            self.layout.addWidget(main_menu_button)

            # Add a button to exit the program
            exit_button = QPushButton("Exit Program")
            exit_button.setStyleSheet("font-size: 16px; padding: 10px;")
            exit_button.clicked.connect(self.exit_program)
            self.layout.addWidget(exit_button)

    def go_to_data_review(self):
        """
        Description: Navigate to the DataReviewPage and load the result file.
        Input: None
        Output: None
        """
        if self.result_file_path:
            self.restart_page()
            self.parent.data_review_page.read_and_display_data(self.result_file_path)
            self.parent.stack.setCurrentWidget(self.parent.data_review_page)
        else:
            QMessageBox.warning(self, "File Missing", "Result file path is not available.")

    def go_to_main_menu(self):
        """
        Description: Navigate back to the main menu.
        Input: None
        Output: None
        """
        self.restart_page()
        self.parent.stack.setCurrentWidget(self.parent.main_menu)

    # Going back for another trial
    def go_back_to_trial(self):
        """
        Description: Navigate back to the trial page.
        Input: None
        Output: None
        """
        self.restart_page()
    
        #  Switch back to CalibrationPage
        self.parent.stack.setCurrentWidget(self.parent.calibration_page)

        print("CalibrationPage and EditPage have been fully reset and reloaded.")

    def exit_program(self):
        """
        Description: Exit the program.
        Input: None
        Output: None
        """
        self.restart_page()
        QApplication.quit()

    def previous_image(self,text):
        """
        Description: Load the previous image in the image list.
        Decrement the image index and update the information label.
        Remove the last line from the results file.
        Load the previous image with a message to click on the puck.
        Input: text - text to display in the direction label
        Output: None
        """
        if self.image_index > 1:
            self.image_index -= 1
            text = "Loaded previous image please click on the puck"
            self.info_label.setText(f"Image Trial [{self.image_index} out of Total Images [{len(self.image_list) - 1}] ] | Radial: None | Y-axis: None | X-axis: None")
            self.file_manager.remove_last_line(self.result_file_path)
            self.radial = None
            self.xaxis = None
            self.yaxis = None
            self.load_image(self.image_index, text)
        else:
            QMessageBox.warning(self, "Start of Images", "This is the first image.")

    def create_files_list(self, folder_path, image_path):
        """
        Description: Create the list of image files in the selected folder.
        Create the Results folder and Results file.
        Input: folder_path - path to the folder containing images
               image_path - path to the selected image
        Output: None
        """
        # Constants for results folder and file
        RESULTS_FOLDER_NAME = "Results"
        RESULTS_FILE_NAME = "Results_File.txt"


        # Ensure image_path is the first in the image list
        self.image_list = [
            os.path.normpath(os.path.join(folder_path, f))
            for f in os.listdir(folder_path)
            if f.lower().endswith((".png", ".jpg", ".jpeg", ".bmp"))
        ]

        # Normalize image_path for comparison
        normalized_image_path = os.path.normpath(image_path)

        # Remove image_path if it exists and insert it at the beginning

        if normalized_image_path in self.image_list:
            self.image_list.remove(normalized_image_path)
        self.image_list.insert(0, normalized_image_path)

        # Create Results folder
        results_folder_path = os.path.join(folder_path, RESULTS_FOLDER_NAME)
        if not os.path.exists(results_folder_path):
            self.result_folder_path = self.file_manager.create_folder(folder_path, folder_name=RESULTS_FOLDER_NAME)
        else:
            self.result_folder_path = results_folder_path

        # Create Results file
        results_file_path = os.path.join(self.result_folder_path, RESULTS_FILE_NAME)
        if not os.path.exists(results_file_path):
            self.result_file_path = self.file_manager.create_text_file(self.result_folder_path, file_name=RESULTS_FILE_NAME)
        else:
            self.result_file_path = results_file_path

    def set_data(self, scaling_factor, folder_path, image_path, axis_orientation):
        """
        Description: Set the data required for image editing.
        Input: scaling_factor - scaling factor for the image
               folder_path - path to the folder containing images
               image_path - path to the selected image
               result_file_path - path to the result file
        Output: None
        """
        self.scaling_factor = scaling_factor
        self.folder_path = folder_path
        self.axis_orientation = axis_orientation
        self.create_files_list(folder_path, image_path)
        self.track_clicks = 2
        self.image_viewer.track_clicks = self.track_clicks
        self.load_image(self.image_index, "Please click on the center")

        # check the value in the axis_orientation by printing it
        print(self.axis_orientation) 


    def restart_page(self):
        """
        Description: Clear memory to start a new trial 
        Input: None
        Output: None
        """
        parent_stack = self.parent.stack  # Get reference to QStackedWidget

        # Remove existing instances of EditPage and CalibrationPage from QStackedWidget
        parent_stack.removeWidget(self.parent.edit_page)
        parent_stack.removeWidget(self.parent.calibration_page)

        # Delete the old instances to free memory
        self.parent.edit_page.deleteLater()
        self.parent.calibration_page.deleteLater()

        #  Create fresh instances of both pages
        self.parent.calibration_page = CalibrationPage(self.parent)
        self.parent.edit_page = EditPage(self.parent)

        #  Add the new instances back to QStackedWidget
        parent_stack.addWidget(self.parent.calibration_page)
        parent_stack.addWidget(self.parent.edit_page)

    def no_image(self):
        """
        Description: When trial with no existing picture exists, user presses this button
                     to add 'zero' data to resuts

        Input: None
        """
        self.radial, self.xaxis, self.yaxis = "N/A", "N/A", "N/A" # Placeholder data
        
        # Add data to results file 
        self.file_manager.append_axis_data(
            self.result_file_path, self.image_index, self.radial, self.yaxis, self.xaxis
        )
       
        if self.center_point == None:
            self.image_index += 1
            self.info_label.setText(f" On Trial [{self.image_index}] out of [{len(self.image_list) - 1}] || Previous Trial Values: || Radial: {self.radial} | X-axis: {self.xaxis} | Y-axis: {self.yaxis}")
            self.track_clicks = 2
            self.image_viewer.track_clicks = self.track_clicks
            self.load_image(self.image_index, "Previous trial image DNE. Next image loaded")
        else:
            self.next_image("Previous trial image DNE. Next image loaded") # Move on to next trial image
            
    def invalid_trial(self):
        """
        Description: When trial exists when puck lies outside of valid grid area, user
                     presses button to add outlier to results data
        Input: None
        Input: None
        """
        self.radial, self.xaxis, self.yaxis = 99999, 99999, 99999 # Placheholder data

        # Add data to results files
        self.file_manager.append_axis_data(
            self.result_file_path, self.image_index, self.radial, self.yaxis, self.xaxis
        )

        if self.center_point == None:
            self.image_index += 1
            self.info_label.setText(f" On Trial [{self.image_index}] out of [{len(self.image_list) - 1}] || Previous Trial Values: || Radial: {self.radial} | X-axis: {self.xaxis} | Y-axis: {self.yaxis}")
            self.track_clicks = 2
            self.image_viewer.track_clicks = self.track_clicks
            self.load_image(self.image_index, "Previous trial was out of bounds. Next image loaded")
        else:
            self.next_image("Previous trial was out of bounds. Next image loaded") # Move on to next trial image