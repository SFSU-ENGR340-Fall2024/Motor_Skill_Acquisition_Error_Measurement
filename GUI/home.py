import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QVBoxLayout, QFileDialog

class FolderSelect(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()

    def PickFolder(self):
        folder_path  = QFileDialog.getExistingDirectory(self, 'Select Folder')

    def ExitProgram(self):
        sys.exit()

    def UI(self):
        # initialize 'select folder' button
        select_folder_button = QPushButton('Select Folder')
        select_folder_button.clicked.connect(self.PickFolder)
        select_folder_button.setStyleSheet('font-size: 20px')

        # initialize 'exit' button
        exit_button = QPushButton('Exit')
        exit_button.clicked.connect(self.ExitProgram)
        exit_button.setStyleSheet('font-size: 20px')

        # arrange buttons
        vbox = QVBoxLayout()
        vbox.addWidget(select_folder_button)
        vbox.addWidget(exit_button)

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
