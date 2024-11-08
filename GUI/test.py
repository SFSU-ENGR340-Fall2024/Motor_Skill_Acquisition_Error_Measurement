import sys
from gui import GUI
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QLabel,
                             QStackedWidget, QVBoxLayout, QFileDialog)

class Test(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):
        self.page = QWidget()
        self.back = QPushButton('Back')
        self.back.setStyleSheet('font-size: 20px')
        # self.back.clicked.connect(GUI.back_button)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.back)
        self.setLayout(self.layout)

        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Error Measurement Tool')
        self.show()

    
if __name__ == '__main__':
    app = QApplication(sys.argv) # create application object
    ex = Test() # create GUI object
    sys.exit(app.exec_()) # execute app