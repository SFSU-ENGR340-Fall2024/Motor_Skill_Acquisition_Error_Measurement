############################################################################################
# Project Name: Motor Skill Acquisition Error Management System (San Francisco State University Project 2024) 
# 
# Filename: CalibrationPage.py
# 
# Authors: Milton Tinoco, Ethan Weldon, Joshua Samson, Michael Cabrera
#
# Last Update: 12/08/2024
#
# File Description:
# This file contains the code for the calibration page of the application. 
# The calibration page allows users to select a folder of images, choose a calibration image, horizontal and vertical axis,
# and set the distance between two points in the image to calculate a scaling factor for real-world measurements.
# It also reslect the points and axis if the user made a mistake.
# Then proceed to the image editing page to apply the scaling factor to other images.
#
############################################################################################

# Import necessary libraries

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QGraphicsView, QGraphicsScene,
    QGraphicsPixmapItem, QVBoxLayout, QWidget, QPushButton, QFileDialog, QLabel
)
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QLineEdit, QMessageBox
from PyQt5.QtGui import QPixmap, QPen, QPainter, QFont
from PyQt5.QtCore import Qt, QLineF,QPoint
from file_manger_class import FileManager
from calculation_class import CalculationsManager
from image_interface import ImageView
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import QTimer
import os
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


# Class: CalibrationPage
# Description: 
# This class represents the calibration page of the application.
# It allows users to select a folder of images, choose a calibration image,
# and set the distance between two points in the image to calculate a scaling factor for real-world measurements.
# The user can then proceed to the image editing page to apply the scaling factor to other images.

# Class: CalibrationPage
class CalibrationPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Set the parent widget
        self.parent = parent

        # Initialize file and calculations managers
        self.file_manager = FileManager()
        self.calculations_manager = CalculationsManager()

        # Set vertical layout
        self.layout = QVBoxLayout(self)
        self.button_layout = QHBoxLayout()

        # Load image information
        self.image_folder = os.path.join(os.getcwd(), "programImages")
        self.image_files = ["graph1.png", "graph2.png", "graph3.png", "graph4.png"]
        self.axis_orientation = 0  # Start at the first image

        # Direction label
        self.direction_label = QLabel("Please select a folder with image set, then select a calibration image.") 
        self.direction_label.setAlignment(Qt.AlignCenter)
        self.direction_label.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 20px;")
        self.layout.addWidget(self.direction_label)

        # Folder selection button
        self.select_folder_button = QPushButton("Select Folder")
        self.select_folder_button.clicked.connect(self.select_folder)
        self.button_layout.addWidget(self.select_folder_button)

        # Image selection button
        self.select_image_button = QPushButton("Reselect Image")
        self.select_image_button.setEnabled(False)
        self.select_image_button.clicked.connect(self.select_image)
        self.button_layout.addWidget(self.select_image_button)
        self.select_image_button.hide()

        # Reselect points button
        self.reselect_points_button = QPushButton("Reselect Points")
        self.reselect_points_button.setEnabled(False)
        self.reselect_points_button.clicked.connect(self.reselect_points)
        self.button_layout.addWidget(self.reselect_points_button)
        self.reselect_points_button.hide()

        self.layout.addLayout(self.button_layout)

        #####################################################
        # Graph Display Section with Buttons NEXT to Image
        #####################################################

        # Create a horizontal layout for the graph and buttons
        graph_layout = QHBoxLayout()

        # Left button (previous graph)
        self.left_button = QPushButton("⬅ Spin Orientation \n" "Left")
        self.left_button.clicked.connect(self.previous_image)

        # QLabel for displaying the graph
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setScaledContents(True)
        self.image_label.setFixedSize(150, 100)  # Set fixed size for consistency
        self.load_image()  # Load the initial image

        # Right button (next graph)
        self.right_button = QPushButton("Spin Orientation ➡\n" "Right")
        self.right_button.clicked.connect(self.next_image)

        # Add elements to the horizontal layout (Buttons on sides, Image in center)
        graph_layout.addWidget(self.left_button)  # Add left button
        graph_layout.addWidget(self.image_label)  # Add image in center
        graph_layout.addWidget(self.right_button)  # Add right button
    
        # Add the graph layout to the main layout
        self.layout.addLayout(graph_layout)
        
        # Hide 
        
        self.hide_graph_and_buttons()
        
        #####################################################
        # Distance Input Section
        #####################################################

        # Distance input field
        self.distance_input = QLineEdit()
        self.distance_input.setPlaceholderText("Enter distance between points in cm (e.g., 10)")
        self.distance_input.setStyleSheet("font-size: 20px")
        self.distance_input.setEnabled(False)  # Enable after selecting two points
        self.distance_input.installEventFilter(self)  # Enable Enter key press event
        self.layout.addWidget(self.distance_input)
        self.distance_input.returnPressed.connect(self.handle_enter_pressed)
        self.distance_input.hide()  # Initially hidden

        #####################################################
        # Image Viewer for Point Selection
        #####################################################

        # Image viewer for calibration selection
        self.image_viewer = ImageView()
        self.image_viewer.track_clicks = 2  # Track two clicks
        self.layout.addWidget(self.image_viewer)

        # Assign the layout to the widget
        self.setLayout(self.layout)

        #####################################################
        # Variables for Selection Tracking
        #####################################################

        self.folder_path = None  # Store selected folder path
        self.image_path = None  # Store selected image path
        self.clicked_points = []  # Store clicked points
        # Connect ImageView click signal
        self.image_viewer.point_clicked.connect(self.handle_point_clicked)
        
    def hide_graph_and_buttons(self):
        """Hides the graph image and navigation buttons."""
        self.image_label.hide()
        self.left_button.hide()
        self.right_button.hide()
        
    def show_graph_and_buttons(self):
        """Shows the graph image and navigation buttons."""
        self.image_label.show()
        self.left_button.show()
        self.right_button.show()

    def load_image(self):
            """Loads the current graph based on index."""
            image_path = os.path.join(self.image_folder, self.image_files[self.axis_orientation])

            if not os.path.exists(image_path):
                print(f"❌ Error: Image not found at {image_path}")
                self.image_label.setText(f"Error loading image: {self.image_files[self.axis_orientation]}")
                return

            pixmap = QPixmap(image_path)
            if pixmap.isNull():
                print(f"❌ Error: Unable to load image {image_path}")
                self.image_label.setText(f"Error loading image: {self.image_files[self.axis_orientation]}")
            else:
                self.image_label.setPixmap(pixmap)  # Display image

    def next_image(self):
        """Go to the next image in the list."""
        print("Before",self.axis_orientation)
        self.axis_orientation = (self.axis_orientation + 1) % len(self.image_files)
        print(self.axis_orientation)
        self.load_image()
    

    def previous_image(self):
        """Go to the previous image in the list."""
        print("Before",self.axis_orientation)
        self.axis_orientation = (self.axis_orientation - 1) % len(self.image_files)
        print(self.axis_orientation)
        self.load_image()

    # Method (handle_enter_pressed)
    # Description:
    # This method handler after the user presses the Enter key in the distance input field.
    # It validates the entered distance, calculates the scaling factor based on the selected distance between points,
    # update the direction label with the distance entered, pixel distance, and scaling factor,
    # Input: self
    # Output: None'

    def handle_enter_pressed(self):
        """Handle pressing Enter in the distance input field."""
        try:
            # Get and validate the entered distance
            distance = float(self.distance_input.text())
            if distance <= 0:
                raise ValueError("Distance must be a positive number.")
            
            # Calculate pixel distance between the clicked points
            pixel_distance = self.calculations_manager.calculate_pixel_distance(
                self.clicked_points[0][0],
                self.clicked_points[0][1],
                self.clicked_points[1][0],
                self.clicked_points[1][1]
            )

            # Calculate the scaling factor
            scaling_factor = self.scaling_factor = self.calculations_manager.calculate_scaling_factor(
                distance, pixel_distance
            )

            # Transition to the next page after a delay
            QTimer.singleShot(500, lambda: self.next_page(scaling_factor))

        except ValueError as e:
            # Display an error message box with the specific issue
            QMessageBox.warning(self, "Invalid Input", str(e))


    # Method (next_page)
    # Description:
    # This method switches to the next page after a delay of 2 seconds.
    # Input: self
    # Output: None
    def next_page(self, scaling_factor):

        folder_path = self.folder_path
        image_path = self.image_path
        axis_orientation = self.axis_orientation
        scaling_factortemp = scaling_factor
        # Transition to the next page (image editing page)
        # pass, scaling_factor, folder_path, image_path, axis
        self.parent.edit_page.set_data(scaling_factortemp, folder_path,image_path,axis_orientation)
        self.parent.stack.setCurrentWidget(self.parent.edit_page)

    
    # Method (reselect_points)
    # Description:
    # This method allows the user to reselect the two points in the image to set the distance.
    # It clears the clicked points list, resets the image viewer, and prompts the user to select new points.
    # Input: self
    # Output: None

    def reselect_points(self):
        self.hide_graph_and_buttons()
        self.clicked_points = [] # Clear the clicked points
        self.reselect_points_button.setEnabled(False) # Disable the button
        self.image_viewer.click_list = [] # Clear the clicked points
        self.direction_label.setText("Please select new two points to set the distance")
        self.image_viewer.load_image(self.image_path) # Reload the image
        


    # Method (handle_point_clicked)
    # Description:
    # This method handles the clicked points on the image viewer.
    # It checks if the clicked point is too close to an already clicked point and displays a warning message.
    # If two points are selected, it enables the next steps and prompts the user to select the vertical axis.
    # Input: self, x, y (coordinates of the clicked point)
    # Output: None

    def handle_point_clicked(self, x, y):
        # Check if the clicked point is too close to an already clicked point
        for point in self.clicked_points:
            # If the distance between the clicked point and an already clicked point is less than 10 pixels
            if abs(point[0] - x) < 1 and abs(point[1] - y) < 1: 
                QMessageBox.warning(self, "Invalid Selection", "You cannot select the same spot or too close to it.")
                self.reselect_points() # Reselect the points
                return
            
        # Append the clicked point to the clicked points list

        if (x, y) not in self.clicked_points:
            self.clicked_points.append((x, y))

        # If two points are selected, enable the next steps
        # and prompt the user to select the vertical axis
        if len(self.clicked_points) == 2: 
            self.reselect_points_button.setVisible(True) # Show the reselect points button
            self.reselect_points_button.setEnabled(True) # Enable the reselect points button
            self.direction_label.setText("Please select the orientation of the X, Y axis\n" "Then enter distance between the two selected points") # Prompt the user to select the vertical axis
            # Show the graph images
            self.show_graph_and_buttons()
            self.distance_input.setVisible(True) # Show the distance input field
            self.distance_input.setEnabled(True) # Enable the distance input field  
            
    # Method (select_folder)
    # Description:
    # This method opens a dialog to select a folder containing images.
    # It updates the folder path label and enables the select image button.
    # Input: self
    # Output: None

    def select_folder(self):
        """Open a dialog to select a folder."""
        # Open a dialog to select a folder
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder_path:
            self.folder_path = folder_path # Store the selected folder path
            self.select_image_button.setEnabled(True)# Enable the select image button
            self.select_image_button.setVisible(True)#  Show the select image button
            self.select_image() # Call the select_image method

    # Method (select_image)
    # Description:
    # This method opens a dialog to select an image from the selected folder.
    # It loads the selected image in the image viewer and prompts the user to select two points to set the distance.
    # Input: self
    # Output: None
    def select_image(self):
        
            self.image_viewer.click_list = [] # Clear the clicked points
            self.clicked_points = [] # Clear the clicked points
            """Open a dialog to select an image from the selected folder."""
            if not self.folder_path:
                return
            # Open a dialog to select an image from the selected folder
            options = QFileDialog.Options()
            options |= QFileDialog.ReadOnly
            image_path, _ = QFileDialog.getOpenFileName(
                self,
                "Select Image",
                self.folder_path,
                "Images (*.png *.jpg *.jpeg *.bmp)",
                options=options
            )
            # If an image is selected, load it in the image viewer
            if image_path:
                self.image_path = image_path # Store the selected image path
                self.image_viewer.load_image(image_path) # Load the selected image in the image viewer
                self.direction_label.setText("Please select two points to set the distance") # Prompt the user to select two points
                self.select_folder_button.setText("Reselect Folder")# Change the text of the select folder button

