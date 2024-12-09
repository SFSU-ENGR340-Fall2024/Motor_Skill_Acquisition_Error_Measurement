import cv2
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QPoint, QTimer, pyqtSignal

from data_class import DataClass
from calculation_class import CalculationsManager
from file_manger_class import FileManager


class ClickableLabel(QLabel):
    """A custom QLabel that emits the coordinates of mouse clicks."""
    point_clicked = pyqtSignal(QPoint)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.point_clicked.emit(event.pos())


class EditPage(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.image_file_list = []
        self.calibration_distance = None
        self.pixel_distance = None
        self.image = None
        self.scaled_width = 0
        self.scaled_height = 0
        self.dataclass_object_list = []
        self.folder_path = None
        self.current_index = 0
        self.clicked_points = []
        self.center_point = None
        self.puck_point = []
        self.file_path = None

        # Create calculations manager and file manager objects
        self.calculations_manager = CalculationsManager()
        self.file_manager = FileManager()

        # Create main layout as a horizontal layout
        main_layout = QHBoxLayout()

        # Create a vertical layout for the image and controls
        image_layout = QVBoxLayout()

        # Add a label to display the image
        self.image_label = ClickableLabel("Image will appear here.")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet("font-size: 20px")
        self.image_label.point_clicked.connect(self.handle_click)
        image_layout.addWidget(self.image_label)

        # Add a label to provide instructions
        self.info_label = QLabel("Click on the center of the image to mark it.")
        self.info_label.setAlignment(Qt.AlignCenter)
        self.info_label.setStyleSheet("font-size: 20px")
        image_layout.addWidget(self.info_label)

        # Add navigation buttons
        self.back_button = QPushButton("Back to Main Menu")
        self.back_button.setStyleSheet("font-size: 20px")
        self.back_button.clicked.connect(
            lambda: parent.stack.setCurrentWidget(parent.main_menu)
        )
        image_layout.addWidget(self.back_button)

        self.previous_button = QPushButton("Previous Image")
        self.previous_button.setStyleSheet("font-size: 20px")
        self.previous_button.clicked.connect(self.previous_image)
        image_layout.addWidget(self.previous_button)

        # Add the image layout to the main layout
        main_layout.addLayout(image_layout)

        # Create a vertical layout for the information panel
        self.info_panel = QVBoxLayout()

        # Add labels for the calculations
        self.calculations_label = QLabel("Calculations:")
        self.calculations_label.setStyleSheet("font-size: 20px")
        self.calculations_label.setAlignment(Qt.AlignLeft)
        self.info_panel.addWidget(self.calculations_label)

        self.z_label = QLabel("Z: Not calculated")
        self.z_label.setAlignment(Qt.AlignLeft)
        self.z_label.setStyleSheet("font-size: 20px")
        self.info_panel.addWidget(self.z_label)

        self.x_label = QLabel("X: Not calculated")
        self.x_label.setAlignment(Qt.AlignLeft)
        self.x_label.setStyleSheet("font-size: 20px")
        self.info_panel.addWidget(self.x_label)

        self.y_label = QLabel("Y: Not calculated")
        self.y_label.setAlignment(Qt.AlignLeft)
        self.y_label.setStyleSheet("font-size: 20px")
        self.info_panel.addWidget(self.y_label)

        self.error_label = QLabel("Error Percentage: Not calculated")
        self.error_label.setAlignment(Qt.AlignLeft)
        self.error_label.setStyleSheet("font-size: 20px")
        self.info_panel.addWidget(self.error_label)

        # Add the info panel to the main layout
        main_layout.addLayout(self.info_panel)

        # Set the main layout
        self.setLayout(main_layout)

    def previous_image(self):
        """Move to the previous image."""
        if self.current_index > 0:
            self.current_index -= 1
            self.set_data_next(self.current_index)
        else:
            self.info_label.setText("This is the first image.")
            print("Already at the first image.")

    def set_data(self, current_index, image_file_list, pixel_distance, calibration_distance, folder_path):
        """Set the list of images and calibration distance."""
        self.image_file_list = image_file_list
        self.pixel_distance = pixel_distance
        self.calibration_distance = calibration_distance
        self.folder_path = folder_path
        self.current_index = current_index
        self.dataclass_object_list = [None] * len(self.image_file_list)

        # Initialize the first DataClass object
        dataobject = DataClass(image_file_list[0])
        dataobject.set_image_list(image_file_list)
        dataobject.set_position_index(0)
        self.dataclass_object_list[0] = dataobject
        self.current_index = current_index + 1
        # Set the first image
        self.set_data_next(current_index)

    def set_data_next(self, current_index):
        """Set the data for the next image."""
        self.current_index = current_index
        self.puck_point = []
        self.clicked_points = []
        self.load_image()

    def load_image(self):
        """Load and display the current image."""
        if 0 <= self.current_index < len(self.image_file_list):
            image_path = self.image_file_list[self.current_index]
            self.image = cv2.imread(image_path)

            if self.image is not None:
                # Create a DataClass object if it doesn't exist
                if self.dataclass_object_list[self.current_index] is None:
                    dataclass_object = DataClass(image_path)
                    dataclass_object.set_image_list(self.image_file_list)
                    dataclass_object.set_position_index(self.current_index)
                    self.dataclass_object_list[self.current_index] = dataclass_object

                # Convert BGR to RGB and prepare for display
                rgb_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
                height, width, channels = rgb_image.shape
                bytes_per_line = channels * width
                q_image = QImage(rgb_image.data, width, height, bytes_per_line, QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(q_image)

                # Scale the image
                fixed_width = 1500
                fixed_height = 800
                scaled_pixmap = pixmap.scaled(fixed_width, fixed_height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self.scaled_width = scaled_pixmap.width()
                self.scaled_height = scaled_pixmap.height()

                self.image_label.setPixmap(scaled_pixmap)
                self.clicked_points = []

                # Automatically mark the center point if it has been set
                if self.center_point:
                    self.clicked_points.append(QPoint(self.center_point.x(), self.center_point.y()))
                    self.draw_points()  # Automatically draw the center point
                    self.info_label.setText("Please click on the puck.")

            else:
                self.image_label.setText("Failed to load image.")
        else:
            self.image_label.setText("No images available.")

    def handle_click(self, point):
        """Handle the click and update the image after each click."""
        if len(self.clicked_points) >= 2:
            return

        label_width = self.image_label.width()
        label_height = self.image_label.height()
        pixmap = self.image_label.pixmap()

        if pixmap is None:
            return

        # Calculate offsets and map to original dimensions
        offset_x = (label_width - self.scaled_width) // 2
        offset_y = (label_height - self.scaled_height) // 2
        adjusted_x = point.x() - offset_x
        adjusted_y = point.y() - offset_y

        if 0 <= adjusted_x < self.scaled_width and 0 <= adjusted_y < self.scaled_height:
            original_x, original_y = self.map_to_original(adjusted_x, adjusted_y)
            self.clicked_points.append(QPoint(original_x, original_y))
            self.draw_points()

            if len(self.clicked_points) == 1:
                self.info_label.setText("Please click on the puck.")
            elif len(self.clicked_points) == 2:
                self.info_label.setText("Thank you for selecting the puck and center")
                self.update_calculations()
                QTimer.singleShot(2000, self.update_after_delay)
        else:
            print("Click outside image area.")

    def map_to_original(self, x, y):
        """Map the adjusted point to the original image dimensions."""
        if self.image is None:
            return 0, 0

        original_height, original_width = self.image.shape[:2]
        x_scale = original_width / self.scaled_width
        y_scale = original_height / self.scaled_height
        original_x = int(x * x_scale)
        original_y = int(y * y_scale)
        return original_x, original_y

    def draw_points(self):
        """Draw points on the image and update the QLabel."""
        if self.image is not None:
            temp_image = self.image.copy()
            for point in self.clicked_points:
                cv2.circle(temp_image, (point.x(), point.y()), 5, (0, 255, 0), -1)

            rgb_image = cv2.cvtColor(temp_image, cv2.COLOR_BGR2RGB)
            height, width, channels = rgb_image.shape
            bytes_per_line = channels * width
            q_image = QImage(rgb_image.data, width, height, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(q_image).scaled(
                self.image_label.width(),
                self.image_label.height(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            self.image_label.setPixmap(pixmap)

    def update_calculations(self):
        """Update the calculations in the info panel."""
        if len(self.clicked_points) == 2:
            x1, y1 = self.clicked_points[0].x(), self.clicked_points[0].y()
            x2, y2 = self.clicked_points[1].x(), self.clicked_points[1].y()

            scaling_factor = self.calculations_manager.calculate_scaling_factor(
                self.calibration_distance, self.pixel_distance
            )
            x, y = self.calculations_manager.calculate_real_world_coordinates(x1, y1, x2, y2, scaling_factor)
            z = self.calculations_manager.calculate_error(x1, y1, x2, y2, scaling_factor)
            error_percentage = (z / 100)

            self.dataclass_object_list[self.current_index].set_real_distance_measurement(z)
            self.dataclass_object_list[self.current_index].set_real_world_x_diff(x)
            self.dataclass_object_list[self.current_index].set_real_world_y_diff(y)
            self.dataclass_object_list[self.current_index].set_real_world_percentage(error_percentage)

            self.x_label.setText(f"X: {x:.2f}")
            self.y_label.setText(f"Y: {y:.2f}")
            self.z_label.setText(f"Z: {z:.2f}")
            self.error_label.setText(f"Error Percentage: {error_percentage:.2f}%")

    def update_after_delay(self):
        """Perform actions after a 2-second delay."""
        if self.current_index == 0:
            self.file_path = self.file_manager.create_text_file(self.folder_path)
            self.center_point = self.clicked_points[0]

        self.file_manager.append_to_text_file(
            self.file_path,
            content=(
                f"Image trial {self.dataclass_object_list[self.current_index].get_position_index() + 1} "
                f"x value: {self.dataclass_object_list[self.current_index].get_real_world_x_diff()} "
                f"y value: {self.dataclass_object_list[self.current_index].get_real_world_y_diff()} "
                f"z value: {self.dataclass_object_list[self.current_index].get_real_distance_measurement()} "
                f"error percentage: {self.dataclass_object_list[self.current_index].get_real_world_percentage()}\n"
            )
        )
        self.current_index += 1
        self.set_data_next(self.current_index)
