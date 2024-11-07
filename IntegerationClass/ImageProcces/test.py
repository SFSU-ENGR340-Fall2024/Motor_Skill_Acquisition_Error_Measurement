import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QLabel,
                             QStackedWidget, QVBoxLayout, QFileDialog, QTextEdit)

class Test2(QWidget):
    def __init__(self):
        super().__init__()
        self.UserInput()

    def UserInput(self):
        self.page = QWidget()   

        # Initialize Text box
        self.input = QTextEdit()
        self.input.setPlaceholderText('Enter Distance in meters (m)')
        self.input.setStyleSheet('font-size: 20px')

        # Initialize Confirm Button
        self.confirm = QPushButton('confirm')
        self.confirm.setStyleSheet('font-size: 20px')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.input)
        self.layout.addWidget(self.confirm)
        self.setLayout(self.layout)

        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('Error Measurement Tool')
        # self.show()

    
if __name__ == '__main__':
    app = QApplication(sys.argv) # create application object
    ex = Test2() # create GUI object
    sys.exit(app.exec_()) # execute app