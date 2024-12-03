
import sys
import cv2
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QLabel, QStackedWidget,
)
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from PyQt5.QtCore import Qt, QPoint


class DataReviewPage(QWidget):
    def __init__(self, parent):
        super().__init__()
        layout = QVBoxLayout()

        # Label for data review
        self.data_label = QLabel("Data Review Page")
        self.data_label.setAlignment(Qt.AlignCenter)
        self.data_label.setStyleSheet("font-size: 20px")
        layout.addWidget(self.data_label)

        # Button to return to the main menu
        self.back_button = QPushButton("Back to Main Menu")
        self.back_button.setStyleSheet("font-size: 20px")
        self.back_button.clicked.connect(
            lambda: parent.stack.setCurrentWidget(parent.main_menu)
        )
        layout.addWidget(self.back_button)

        self.setLayout(layout)