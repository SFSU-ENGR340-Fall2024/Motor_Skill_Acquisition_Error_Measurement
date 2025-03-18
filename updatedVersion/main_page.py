############################################################################################
# Project Name: Motor Skill Acquisition Error Management System 
# 
# Filename: main_page.py
# 
# Current Authors: Milton Tinoco, Joshua Samson, Michael Cabrera
# Last Update: 3/18/2025
#
# Previous Authors: Milton Tinoco, Ethan Weldon, Joshua Samson, Michael Cabrera
# Last Update: 12/08/24
#
# Project Description:
# This project is an image editing tool designed to calculate real-life measurements
# between points in images. Users select a folder of images, including a calibration image,
# to determine a scaling factor. The tool applies this factor to calculate real-world 
# distances between points in images, displaying the results and saving them in a text file.
#
# File Description:
# This file contains the code for the main window of the application and initializes 
# the main menu, linking it to the calibration, data review, and image editing pages.
#
############################################################################################

# Importing necessary libraries
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QStackedWidget
)
from PyQt5.QtCore import Qt
from calibration_page import CalibrationPage
from data_review_page import DataReviewPage
from image_editing_page import EditPage

# Class: MainWindow
# Description:
# Initializes the main application window and sets up the navigation between the main menu,
# calibration page, data review page, and image editing page.
class MainWindow(QMainWindow):

    # Constructor
    # Initializes the main window and sets the window title and size.
    # Input: None
    # Output: None
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Motor Skill Acquisition Error Management System")  # Set application window title
        self.setGeometry(100, 100, 1600, 900)     # Set default window size
        self.initUI()                            # Initialize the UI components
    
    # Method: initUI
    # Description:
    # Initializes the main window with a stacked layout for navigation.
    # Input: None
    # Output: None
    
    def initUI(self):
        """Initialize the main window with a stacked layout for navigation."""
        self.stack = QStackedWidget() # Create a stacked widget for page navigation
        self.setCentralWidget(self.stack)  # Display the top widget on the stack

        # Add pages to the stack
        self.main_menu = MainMenu(self) # Main menu page
        self.calibration_page = CalibrationPage(self) # Calibration page
        self.edit_page = EditPage(self) # Image editing page
        self.data_review_page = DataReviewPage(self)    # Data review page

        self.stack.addWidget(self.main_menu)          # Main menu page
        self.stack.addWidget(self.calibration_page)   # Calibration page
        self.stack.addWidget(self.edit_page)          # Image editing page
        self.stack.addWidget(self.data_review_page)   # Data review page

        # Connect main menu buttons to switch pages
        self.main_menu.select_button.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.calibration_page)
        )
        self.main_menu.review_button.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.data_review_page)
        )
        self.main_menu.exit_button.clicked.connect(self.close)

# Class: MainMenu
# Description:
# Represents the main menu page with buttons to start image processing, review data, or exit the program.
class MainMenu(QWidget):
    def __init__(self, parent):
        super().__init__()
        layout = QVBoxLayout()  # Set vertical layout for buttons

        # Welcome text
        welcome_label = QLabel("Motor Skill Acquisition Error Management System\n")
        welcome_label.setAlignment(Qt.AlignCenter)
        welcome_label.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 20px;")
        layout.addWidget(welcome_label)

        # Button to start image processing (navigate to calibration page)
        self.select_button = QPushButton("Start Image Processing")

        # Button to review data (navigate to data review page)
        self.review_button = QPushButton("Review Data")

        # Button to exit the application
        self.exit_button = QPushButton("Exit Program")

        # Style all buttons and add to layout
        buttons = [self.select_button, self.review_button, self.exit_button]
        [button.setStyleSheet('font-size: 20px') for button in buttons]
        [layout.addWidget(button) for button in buttons]

        # Set layout margins (right, left, left, bottom)
        layout.setContentsMargins(100, 100, 100, 100)  # Increase bottom margin

        # Apply layout to the main menu
        self.setLayout(layout)

# Main function to run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)   # Initialize the application
    window = MainWindow()          # Create the main window
    window.show()                  # Display the main window
    sys.exit(app.exec_())          # Start the application event loop
