import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QComboBox,
                             QStackedWidget, QVBoxLayout, QFileDialog)

class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()

    def SelectFolder(self):
        QFileDialog.getExistingDirectory(self, 'Select Folder')

    def EndProgram(self):
        sys.exit()

    def UI(self):
        # Initialize Start Button
        start = QPushButton('Start Test')
        start.clicked.connect(self.SelectFolder)
        start.setStyleSheet('font-size: 20px')

        # Initialize Review Button
        review = QPushButton('Review Data')
        review.clicked.connect(self.SelectFolder)
        review.setStyleSheet('font-size: 20px')

        # Initialize Exit Button
        exit_button = QPushButton('Exit')
        exit_button.clicked.connect(self.EndProgram)
        exit_button.setStyleSheet('font-size: 20px')

        # Combine Start and Review buttons
        combine = QComboBox()
        combine.addItems(['Select Folder', 'Start Test', 'Review Data'])
        combine.setStyleSheet('font-size: 20px')

        vbox = QVBoxLayout()
        # vbox.addWidget(combine)
        vbox.addWidget(start)
        vbox.addWidget(review)
        vbox.addWidget(exit_button)

        self.setLayout(vbox)
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Error Measurement Tool')
        self.show()
    
def run():
    app = QApplication(sys.argv)
    ex = GUI()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()