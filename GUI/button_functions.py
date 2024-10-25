import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QVBoxLayout, QFileDialog

class button_funtions:
    def SelectFolder(self):
        QFileDialog.getExistingDirectory(self, 'Select Folder')

    def ExitButton(self):
        sys.exit()

    def StartButton(self):
        pass

    def ReviewButton(self):
        pass

    def BackButton(self):
        pass
