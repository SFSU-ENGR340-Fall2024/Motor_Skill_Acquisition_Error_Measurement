import sys, os, cv2
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QLabel, QDialog,
                             QStackedWidget, QVBoxLayout, QFileDialog, QTextEdit)
from PyQt5.QtCore import Qt
from DataClassTemp import DataClass

# from ControlClassTemp import ControlClassTemp

class GUI(QWidget): 
    def __init__(self):
        super().__init__()
        self.__folder = None
        # self.last_button = ""
        self.image = None
        self.points = []
        self.__scaleFactor = None
        self.__dist = None
        self.__measurement = None
        self.__puck = None
        self.__center = None
        self.UI()
        self.get_folder()
        # self.set_folder()
        # self.select_folder()
        # self.start_button = None
        # self.review_button()
        # self.back_button()
    
    # Move to Data Class
    def get_folder(self):
        return self.__folder
    
    # Move to Data Class
    def set_folder(self):
        
        self.__folder = QFileDialog.getExistingDirectory(self, 'Select Folder')
        return self.__folder
    
    def select_folder(self):
        """
        Description:
        """
        self.set_folder()
        return self.label.setText(self.get_folder())
    
    def set_start_button(self, function):
        return self.start.clicked.connect(function)
    
    def get_image(self):
        return self.image
    
    def set_image(self):
        image_file, _ = QFileDialog.getOpenFileName(self, "Select Image", self.get_folder())
        self.image = image_file
        return self.image

    def getScaleFactor(self):
        return self.__scaleFactor

    def setScaleFactor(self, factor):
        self.__scaleFactor = factor
        return self.__scaleFactor

    def getMeasurement(self):
        return self.__measurement

    def setMeasurement(self, meas):
        self.__measurement = meas
        return self.__measurement
    
    def getPuck(self):
        return self.__puck

    def setPuck(self, thePuck):
        self.__puck = thePuck
        return self.__puck

    def review_button(self):
        """
        Description:
        """
        # self.csv = self.get_folder() + "/data.csv"
        self.results = self.get_folder() + '/results'
        # os.startfile(self.csv)
        if not os.path.exists(self.results):
            raise FileNotFoundError('Results do not exist for this test')
        
        try:
            return os.startfile(self.results)
        except Exception as e:
            raise Exception("Failed to open Directory")

    def eventFilter(self, source, event):
        """
        Event filter to detect if the Enter key is pressed in the input field.
        """
        if event.type() == event.KeyPress and event.key() == Qt.Key_Return:
            self.window.accept()  # Close the dialog
            return True
        return super().eventFilter(source, event)
    
    def back_button(self):
        """
        Description:
        """
        self.pages.setCurrentIndex(0)
        self.button = "Back"
        return self.button
    
    def get_distance(self):
        """
        Description: Collect user input for distance as data
        """
        self.dist = int(self.input.toPlainText().strip())
        return self.dist
        
    def ExitButton(self):
        """
        Description:
        """
        return sys.exit()

    # UI design
    def UI(self):
        """
        Description: Primary window of user interface. Holds all the pages
                     that will be included in the final program
        """
        # Create page stack
        self.pages = QStackedWidget(self)
        self.home_page = self.Home()
        self.page_2 = self.Page2()
        
        self.pages.addWidget(self.home_page)
        self.pages.addWidget(self.page_2)

        self.label = QLabel('No Folder Selected')
        self.label.setStyleSheet('font-size: 20px')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.pages)

        self.setLayout(self.layout)
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Error Measurement Tool')
        self.show()

    def Home(self):
        """
        Description: Initial page on start-up. Has four functions:
                     - Select Folder: User selects directory of the test folder
                     - Start Test: Perform image processing tests on the images within the selected folder
                     - Review Data: If collected data already exist, view it
                     - Exit: Close the program
        """
        self.page = QWidget()

        # Initialize Select Folder Button
        select = QPushButton('Select Folder')
        select.clicked.connect(self.select_folder)
        select.setStyleSheet('font-size: 20px')

        # Initialize Start Button
        self.start = QPushButton('Start Test')
        self.start.setStyleSheet('font-size: 20px')

        # Initialize Review Button
        review = QPushButton('Review Data')
        review.clicked.connect(self.review_button)
        review.setStyleSheet('font-size: 20px')

        # Initialize Exit Button
        exit_button = QPushButton('Exit')
        exit_button.clicked.connect(self.ExitButton)
        exit_button.setStyleSheet('font-size: 20px')

        # Arrange buttons to vertical layout
        vbox = QVBoxLayout()
        vbox.addWidget(select)
        vbox.addWidget(self.start)
        vbox.addWidget(review)
        vbox.addWidget(exit_button)

        self.page.setLayout(vbox)
        return self.page     
    
    def Page2(self):
        self.page = QWidget()

        # self.scaleFactor = QLabel('Scaling Factor:', self.getScaleFactor())
        self.measurement = QLabel(f"Distance between the points: {self.getMeasurement()}")
        self.measurement.setStyleSheet('font-size: 20px')

        self.back = QPushButton('Back to Main Menu')
        self.back.setStyleSheet('font-size: 20px')
        self.back.clicked.connect(self.back_button)

        layout = QVBoxLayout()
        layout.addWidget(self.measurement)
        layout.addWidget(self.back)
        self.page.setLayout(layout)
        return self.page
    
    def DistanceInput(self):
        """
        Description: Pop-up Dialog for user to input desired real-world distance 
                     that the selected points placed on an image represents
        """
        self.window = QDialog(self)
        self.window.setGeometry(100, 100, 300, 200)
        self.window.setWindowTitle('EnterDistance')

        # Initialize Text box
        self.input = QTextEdit()
        self.input.setPlaceholderText('Enter Distance in meters (m)')
        self.input.setStyleSheet('font-size: 20px')
        self.input.installEventFilter(self)
        # self.dist = int(self.input.toPlainText().strip())

        # Initialize Confirm Button
        self.confirm = QPushButton('confirm')
        self.confirm.setStyleSheet('font-size: 20px')
        self.confirm.clicked.connect(self.window.accept)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.input)
        self.layout.addWidget(self.confirm)
        self.window.setLayout(self.layout)

        self.window.exec()

    def drawCross(self, x, y, image):
        """
        Description: Method to draw a cross on the image at place of mouse click
                     Input: x/y coordinates represented as integers
                     Output: Redrawn image with the cross drawn
        """
        # Draw a cross centered at (x, y) on the image
        size = 8  # Half the length of each line in the cross (adjust as needed)
        color = (0, 0, 255)  # Color of the cross
        thickness = 2  # Thickness of the lines

        # Horizontal line
        cv2.line(image, (x - size, y), (x + size, y), color, thickness)
        # Vertical line
        cv2.line(image, (x, y - size), (x, y + size), color, thickness)

    def checkclicks(self, event, x, y, flags, param):
        """
        Description: Method to check left mouse-click location
                     Input: event, x, y, flags, param
                     Output: x, y position of the mouse click
        """
        if event == cv2.EVENT_LBUTTONDOWN:  # Check if left mouse button is clicked
            print("Left mouse button clicked at:", x, y)
            self.drawCross(x, y,self.image)
            self.points.append((x, y))
        else:
            return None
        
    def drawline(self, x1, y1, x2, y2, image):
        """
        Description: Method to draw a line between two points on the image
                     Input: x1, y1, x2, y2 -> x/y coordinates of two selected points
                            image: current working image
                     Output: Redrawn image with the line drawn
        """
        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 1)
        cv2.imshow('Test Image', image)

    def restartimage(self, image, original_image):
        """
        Description: Method to clear the image by reloading the original image
                     Input: image, original_image
                     Output: none
        """
        cv2.destroyAllWindows()
        cv2.waitKey(1)
        image = original_image

    def displaytextrightbottom(self, image, text):
        """
        Description: Method to display text at the bottom of the image with 
                     a transparent background
                     Input: image, text
                     Output: image with text displayed
        """
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


    def displaytextcenter(self, image, text):
        """
        Description: Method to display text at the middle of the image 
                     with a background
                     Input: image, text
                     Output: image with text displayed
        """
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

    """
    Description: Methods to collect the x and y coordinates of the puck
    Input: image
    Output: x, y
    """
    def center_point_collection(self, image):
        """
        Description: Method to collect the x and y coordinates of the puck
                     Input: image
                     Output: x, y
        """
        self.points = []
        self.image = image
        cv2.namedWindow('Center Point Collection Window')  # Create the window
        cv2.setMouseCallback('Center Point Collection Window', self.checkclicks)
        self.displaytextrightbottom( image, "Please click on the center")
        while True:
            cv2.imshow('Center Point Collection Window', self.image)
            if self.points: # Check if center point is capture 
                print("Calibration complete with center point:", self.points )
                break
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Calibration canceled.")
                break
        cv2.waitKey(1000)  
        cv2.destroyAllWindows()  # Close the window
        return self.points 
    
    def puck_point_collection(self, image):
        """
        Description: Method to collect the x and y coordinates of the puck
                     Input: image
                     Output: x, y
        """
        self.points = []
        self.image = image
        cv2.namedWindow('Puck Point Collection Window')
        cv2.setMouseCallback('Puck Point Collection Window', self.checkclicks)
        self.displaytextrightbottom(image,"Please click on the puck")
        while True:
            cv2.imshow('Puck Point Collection Window', self.image)
            if self.points: # Check if center point is capture 
                break
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cv2.waitKey(1000)  
        cv2.destroyAllWindows()  # Close the window
        return self.points 

    def calibration_point_collection(self, image):
        """
        Description: Method to collect the x and y coordinates of the two point for the calibration 
                     Input: image
                     Output: x1, y1, x2, y2
        """
        self.points = []
        self.image = image
        cv2.namedWindow('Calibration Window')  # Create the window
        cv2.setMouseCallback('Calibration Window', self.checkclicks)
        # Set the mouse callback function
        while True:
            cv2.imshow('Calibration Window', self.image)  # Display the image
            # Exit the loop if two points have been selected
            if len(self.points) >= 2:
                print("Calibration complete with points:", image)
                break
            # Wait for a short period to allow for window refresh
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Calibration canceled.")
                break
        cv2.waitKey(1000)  
        cv2.destroyAllWindows()  # Close the window
        return self.points

    def testimage(self, image):
        cv2.imshow('Test Image', image)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()



    def create_window(self, image):
        cv2.namedWindow('Window for calibration')
        cv2.imshow('Window for calibration', image)
   

    

    
# function to run the GUI class
def Start():
    app = QApplication(sys.argv) # create application object
    ex = GUI() # create GUI object
    sys.exit(app.exec_()) # execute app
    return ex

if __name__ == '__main__':
    Start()