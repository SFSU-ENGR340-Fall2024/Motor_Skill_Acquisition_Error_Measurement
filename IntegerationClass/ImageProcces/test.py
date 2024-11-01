import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QLabel,
                             QStackedWidget, QVBoxLayout, QFileDialog)

class Test(QWidget):
    def __init__(self):
        super().__init__()
        self.UserInput()

    def UserInput(self):
        self.page = QWidget
        
        self.prompt = QLabel('Enter Distance')
       

        self.setLayout(self.layout)
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Error Measurement Tool')
        self.show()

if __name__ == 'main':
    app = QApplication(sys.argv) # create application object
    ex = Test() # create GUI object
    sys.exit(app.exec_()) # execute app