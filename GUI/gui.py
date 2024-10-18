import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QComboBox,
                             QStackedWidget, QVBoxLayout, QFileDialog, QLabel)

class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.folder = 0
        self.UI()
        last_button = 0
    
    def get_folder(self):
        return self.folder
    
    def set_folder(self):
        self.folder = QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.pages.setCurrentIndex(1)
    
    def back_button(self):
        self.pages.setCurrentIndex(0)
        
    def ExitButton(self):
        sys.exit()

    # UI design
    def UI(self):
        self.pages = QStackedWidget(self)
        self.home_page = self.Home()
        self.page_2 = self.Page2()

        self.pages.addWidget(self.home_page)
        self.pages.addWidget(self.page_2)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.pages)

        self.setLayout(self.layout)
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Error Measurement Tool')
        self.show()

    def Home(self):
        page = QWidget()
        # Initialize Start Button
        start = QPushButton('Start Test')
        start.clicked.connect(self.set_folder)
        start.setStyleSheet('font-size: 20px')

        # Initialize Review Button
        review = QPushButton('Review Data')
        review.clicked.connect(self.set_folder)
        review.setStyleSheet('font-size: 20px')

        # Initialize Exit Button
        exit_button = QPushButton('Exit')
        exit_button.clicked.connect(self.ExitButton)
        exit_button.setStyleSheet('font-size: 20px')

        # Arrange buttons to vertical layout
        vbox = QVBoxLayout()
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
    app = QApplication(sys.argv) # create application object
    ex = GUI() # create GUI object
    sys.exit(app.exec_()) # execute app