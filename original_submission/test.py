import sys
from PyQt5.QtWidgets import QApplication
from calibration_page import CalibrationPage

app = QApplication(sys.argv) # initialize applicatiton
win = CalibrationPage() # create gui object
win.show()
sys.exit(app.exec()) # run application