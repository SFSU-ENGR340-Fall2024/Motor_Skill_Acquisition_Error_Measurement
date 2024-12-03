import sys
import cv2
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QLabel, QStackedWidget,
)
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from PyQt5.QtCore import Qt, QPoint
from calibration_page import CalibrationPage
from data_review_page import DataReviewPage
from image_editing_page import EditPage



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SFSU Image Editor")
        self.setGeometry(100, 100, 800, 600)
        self.initUI()

    def initUI(self):
        # Create QStackedWidget to hold pages
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Main Menu Page
        self.main_menu = MainMenu(self)
        self.stack.addWidget(self.main_menu)

        # Folder Selection and Calibration Page
        self.calibration_page = CalibrationPage(self)
        self.stack.addWidget(self.calibration_page)

        # Image Editing Page
        self.edit_page = EditPage(self)
        self.stack.addWidget(self.edit_page)

        # Data Review Page
        self.data_review_page = DataReviewPage(self)
        self.stack.addWidget(self.data_review_page)

        # Connect main menu buttons to switch pages
        self.main_menu.select_button.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.calibration_page)
        )
        self.main_menu.review_button.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.data_review_page)
        )
        self.main_menu.exit_button.clicked.connect(self.close)


class MainMenu(QWidget):
    def __init__(self, parent):
        super().__init__()
        layout = QVBoxLayout()

        # Button to select folder and go to image editing page
        self.select_button = QPushButton("Start Image Processing")
        layout.addWidget(self.select_button)
        self.select_button.setStyleSheet("font-size: 20px")
        

        # Button to review data
        self.review_button = QPushButton("Review Data")
        layout.addWidget(self.review_button)
        self.review_button.setStyleSheet("font-size: 20px")

        # Button to exit the program
        self.exit_button = QPushButton("Exit Program")
        layout.addWidget(self.exit_button)
        self.exit_button.setStyleSheet("font-size: 20px")

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
