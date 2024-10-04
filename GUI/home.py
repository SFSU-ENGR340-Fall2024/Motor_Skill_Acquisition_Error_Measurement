import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QVBoxLayout

class FolderSelect(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):
        # initialize buttons
        select_folder_button = QPushButton('Select Folder')
        select_folder_button.setStyleSheet('font-size: 20px')

        back_button = QPushButton('Back')
        back_button.setStyleSheet('font-size: 20px')

        # arrange buttons
        vbox = QVBoxLayout()
        vbox.addWidget(select_folder_button)
        vbox.addWidget(back_button)

        # create window
        self.setLayout(vbox)
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Error Measurement Tool')
        self.show()

def run():
    app = QApplication(sys.argv)
    ex = FolderSelect()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()
