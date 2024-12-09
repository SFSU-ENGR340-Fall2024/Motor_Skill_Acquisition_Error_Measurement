import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QVBoxLayout

class Home(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()

    def GoBack(self):
        pass

    def UI(self):
        # initialize start button
        start_button = QPushButton('Start New Test')
        start_button.setStyleSheet("font-size: 20px")

        # initialize review button
        review_button = QPushButton('Review Previous Test')
        review_button.setStyleSheet("font-size: 20px")
        
        # initialize exit button
        back_button = QPushButton('Back')
        back_button.clicked.connect(self.GoBack)
        back_button.setStyleSheet("font-size: 20px")

        # arrange buttons
        vbox = QVBoxLayout()
        vbox.addWidget(start_button)
        vbox.addWidget(review_button)
        vbox.addWidget(back_button)

        # create window
        self.setLayout(vbox)
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Error Measurement Tool')
        self.show()

def run():
    app = QApplication(sys.argv)
    ex = Home()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()