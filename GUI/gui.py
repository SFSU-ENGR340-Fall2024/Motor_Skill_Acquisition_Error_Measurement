import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QLabel,
                             QStackedWidget, QVBoxLayout, QFileDialog, QLabel)

class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.__folder = ""
        self.last_button = ""
        self.UI()
        self.get_folder()
    
    def get_folder(self):
        return self.__folder
    
    def set_folder(self):
        self.__folder = QFileDialog.getExistingDirectory(self, 'Select Folder')
        return self.__folder
    
    # def get_last_button(self):
    #     return self.__last_button
    
    def select_folder(self):
        self.set_folder()
        # self.last_button = "Select Folder"
        # label_text = self.get_folder()
        self.label.setText(self.get_folder())
        return self.get_folder()
        
    
    def start_button(self):
        self.pages.setCurrentIndex(1)

    def review_button(self):
        self.pages.setCurrentIndex(1)
    
    def back_button(self):
        self.pages.setCurrentIndex(0)
        self.button = "Back"
        return self.button
        
    def ExitButton(self):
        sys.exit()

    # UI design
    def UI(self):
        # Create page stack
        self.pages = QStackedWidget(self)
        self.home_page = self.Home()
        self.page_2 = self.Page2()
        
        self.pages.addWidget(self.home_page)
        self.pages.addWidget(self.page_2)

        self.label = QLabel()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.pages)

        self.setLayout(self.layout)
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Error Measurement Tool')
        self.show()

    def Home(self):
        page = QWidget()

        # Initialize Select Folder Button
        select = QPushButton('Select Folder')
        select.clicked.connect(self.select_folder)
        select.setStyleSheet('font-size: 20px')

        # Initialize Start Button
        start = QPushButton('Start Test')
        start.clicked.connect(self.start_button)
        start.setStyleSheet('font-size: 20px')

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
        vbox.addWidget(start)
        vbox.addWidget(review)
        vbox.addWidget(exit_button)

        page.setLayout(vbox)
        return page     
    
    def Page2(self):
        self.page = QWidget()
        self.back = QPushButton('Back')
        self.back.setStyleSheet('font-size: 20px')
        self.back.clicked.connect(self.back_button)

        layout = QVBoxLayout()
        layout.addWidget(self.back)
        self.page.setLayout(layout)
        return self.page   

    
# function to run the GUI class
def Start():
    app = QApplication(sys.argv) # create application object
    ex = GUI() # create GUI object
    sys.exit(app.exec_()) # execute app
    return ex

if __name__ == '__main__':
    Start()