import os
import cv2
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QLineEdit, QMessageBox
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QSizePolicy
from file_manger_class import FileManager
from calculation_class import CalculationsManager




class CalibrationPage(QWidget):
    def __init__(self, parent):
        super().__init__()
        
        self.parent = parent
        layout = QVBoxLayout()

        # Create a folder manger object 
        self.file_manager = FileManager()

        # Label to display the selected image
        self.image_label = ClickableLabel("Please Select a Folder")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet("font-size: 20px")
        self.image_label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.image_label.setMinimumSize(1000, 800)
        layout.addWidget(self.image_label)

        # Button to select a folder
        self.folder_button = QPushButton("Select Folder")
        self.folder_button.clicked.connect(self.select_folder)
        self.folder_button.setStyleSheet("font-size: 20px")
        layout.addWidget(self.folder_button)

        # Button to re-select the calibration image
        self.reselect_button = QPushButton("Re-select Calibration Image")
        self.reselect_button.setEnabled(False)  # Disabled until a folder is selected
        self.reselect_button.clicked.connect(self.select_image)
        self.reselect_button.setStyleSheet("font-size: 20px")
        layout.addWidget(self.reselect_button)

        # Input field for distance
        self.distance_input = QLineEdit()
        self.distance_input.setPlaceholderText("Enter distance between points in cm (e.g., 10)")
        self.distance_input.setStyleSheet("font-size: 20px")
        self.distance_input.setEnabled(False)  # Enable after selecting two points
        self.distance_input.installEventFilter(self) # Enable Enter key press event (doesn't work)
        layout.addWidget(self.distance_input)

        # Button to confirm distance
        self.confirm_button = QPushButton("Confirm Distance")
        self.confirm_button.setStyleSheet("font-size: 20px")
        self.confirm_button.setEnabled(False)  # Enable after selecting two points
        self.confirm_button.clicked.connect(self.confirm_distance)
        layout.addWidget(self.confirm_button)

        # Button to return to the main menu
        self.back_button = QPushButton("Back to Main Menu")
        self.back_button.setStyleSheet("font-size: 20px")
        self.back_button.clicked.connect(
            lambda: self.parent.stack.setCurrentWidget(self.parent.main_menu)
        )
        layout.addWidget(self.back_button)

        self.setLayout(layout)
        self.image_files = []
        self.current_index = 0
        self.image = None
        self.clicked_points = []
        self.scaled_width = 0
        self.scaled_height = 0
        self.offset_x = 0
        self.offset_y = 0
        self.pixel_distance = None
        self.calibration_distance = None
        self.results_folder = None
        self.scaling_factor = None

        # Connect the custom signal from the clickable label
        self.image_label.point_clicked.connect(self.handle_click)

    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder_path:
            # Initialize FileManager if not already done
            if not hasattr(self, 'file_manager'):
                self.file_manager = FileManager()
            
            # Ensure the "Results" folder is created in the selected folder
            self.results_folder = self.file_manager.create_folder(folder_path, folder_name="Results")
            
            # Populate image_files with images in the selected folder
            self.image_files = [
                os.path.join(folder_path, f)
                for f in os.listdir(folder_path)
                if f.lower().endswith((".png", ".jpg", ".jpeg", ".bmp"))
            ]
            if self.image_files:
                self.reselect_button.setEnabled(True)  # Enable the reselect button
                self.select_image()


    def select_image(self):
        image_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select an Image",
            os.path.dirname(self.image_files[0]),
            "Images (*.png *.jpg *.jpeg *.bmp)"
        )
        if image_path:
            normalized_image_path = os.path.normpath(image_path)
            normalized_image_files = [os.path.normpath(f) for f in self.image_files]
            if normalized_image_path in normalized_image_files:
                self.current_index = normalized_image_files.index(normalized_image_path)
                self.display_image()
            else:
                self.image_label.setText("Selected image is not in the folder.")

    def display_image(self):
        if self.image_files and self.current_index < len(self.image_files):
            image_path = self.image_files[self.current_index]
            self.image = cv2.imread(image_path)
            if self.image is not None:
                rgb_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)

                # Calculate the scaled size and offsets
                pixmap = QPixmap.fromImage(QImage(rgb_image.data, rgb_image.shape[1], rgb_image.shape[0], rgb_image.strides[0], QImage.Format_RGB888))
                scaled_pixmap = pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)

                self.scaled_width = scaled_pixmap.width()
                self.scaled_height = scaled_pixmap.height()

                # Calculate offsets to center the image within the QLabel
                self.offset_x = (self.image_label.width() - self.scaled_width) // 2
                self.offset_y = (self.image_label.height() - self.scaled_height) // 2

                self.image_label.setPixmap(scaled_pixmap)
                self.clicked_points = []
            else:
                self.image_label.setText("Unable to load image.")

    def handle_click(self, point):
        """Handle the click and update the image after each click."""
        # Stop processing if already two points are clicked
        if len(self.clicked_points) == 2:
            return

        # Adjust the click position to account for offsets
        adjusted_x = point.x() - self.offset_x
        adjusted_y = point.y() - self.offset_y

        # Ensure the click is within the image area
        if 0 <= adjusted_x < self.scaled_width and 0 <= adjusted_y < self.scaled_height:
            # Map the adjusted point to the original image coordinates
            original_x, original_y = self.map_to_original(adjusted_x, adjusted_y)
            self.clicked_points.append(QPoint(original_x, original_y))
            self.draw_points()

            # If two points are clicked, print their locations
            if len(self.clicked_points) == 2:
                print(f"Two points selected: {self.clicked_points}")
                self.distance_input.setEnabled(True)
                self.confirm_button.setEnabled(True)
                self.distance_input.setFocus()  # Set focus to allow immediate typing

    def map_to_original(self, x, y):
        """Map the adjusted point to the original image dimensions."""
        if self.image is None:
            return 0, 0

        # Get dimensions of the original image
        original_height, original_width = self.image.shape[:2]

        # Compute scaling factors
        x_scale = original_width / self.scaled_width
        y_scale = original_height / self.scaled_height

        # Map the coordinates
        original_x = int(x * x_scale)
        original_y = int(y * y_scale)

        return original_x, original_y

    def draw_points(self):
        """Draw points on the image and update the QLabel."""
        if self.image is not None:
            # Make a copy of the original image to avoid permanent modification
            temp_image = self.image.copy()
            for point in self.clicked_points:
                # Define the size of the cross
                cross_size = 10
                
                # Draw a cross at each clicked point
                cv2.line(temp_image, 
                        (point.x() - cross_size, point.y()), 
                        (point.x() + cross_size, point.y()), 
                        (0, 0, 255), 2)  # Horizontal line
                cv2.line(temp_image, 
                        (point.x(), point.y() - cross_size), 
                        (point.x(), point.y() + cross_size), 
                        (0, 0, 255), 2)  # Vertical line

            # Convert the updated image to QPixmap and display it
            rgb_image = cv2.cvtColor(temp_image, cv2.COLOR_BGR2RGB)
            height, width, channels = rgb_image.shape
            bytes_per_line = channels * width
            q_image = QImage(rgb_image.data, width, height, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(q_image)
            scaled_pixmap = pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image_label.setPixmap(scaled_pixmap)


    def confirm_distance(self):
            """Handle the confirmed distance input."""
            try:
                self.calibration_distance = float(self.distance_input.text())

                print("Two points already selected.")
                # Determine the distance between the two points
                calculations_manager = CalculationsManager()
                self.pixel_distance = calculations_manager.calculate_pixel_distance(self.clicked_points[0].x(), self.clicked_points[0].y(), self.clicked_points[1].x(), self.clicked_points[1].y())
                self.scaling_factor = calculations_manager.calculate_scaling_factor(self.calibration_distance, self.pixel_distance)
                print (f"Pixel distance: {self.pixel_distance}, Scaling factor: {self.scaling_factor}")
                print (f"Calibration distance: {self.calibration_distance}")

                QMessageBox.information(self,  "Success",  f"Distance set to {self.calibration_distance:.2f} cm. Scaling factor: {self.scaling_factor:.2f}")
                self.distance_input.setEnabled(False)
                self.confirm_button.setEnabled(False)
                # create start index for the dataclass object list
                dataIndex = 0
                self.parent.edit_page.set_data(dataIndex,self.image_files,self.pixel_distance, self.calibration_distance, self.results_folder)
                self.parent.stack.setCurrentWidget(self.parent.edit_page)
            except ValueError:
                QMessageBox.warning(self, "Error", "Please enter a valid number for the distance.")

class ClickableLabel(QLabel):
    """A custom QLabel that emits the coordinates of mouse clicks."""
    from PyQt5.QtCore import pyqtSignal
    point_clicked = pyqtSignal(QPoint)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # Emit the clicked point as a QPoint
            click_position = event.pos()
            print(f"Clicked point: ({click_position.x()}, {click_position.y()})")
            self.point_clicked.emit(click_position)
