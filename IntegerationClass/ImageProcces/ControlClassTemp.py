import sys, cv2
import numpy as np
from classtest import classtest
from DataClassTemp import DataClass
from ImageProcces import ImageProcess
from GUICopy import GUI
from test import Test2
from PyQt5.QtWidgets import QApplication

ImageDisplayWidth = 1500
ImageDisplayHeight = 700
image_path = r"C:/Users/michc/Pictures/Screenshots/Screenshot 2023-10-22 234927.png"

app = QApplication(sys.argv) # create application object
guiObject = GUI()
imageObject = DataClass(image_path, ImageDisplayWidth, ImageDisplayHeight)
process = ImageProcess()
testPage = Test2()
the_dist = None


def calibrate_system(Object):
    # Collection of points for calibration
    imageObject.set_points(guiObject.calibration_point_collection(Object.get_resized_image()))
    cal_coord = Object.get_points()
    print("Calibration points:", Object.get_points())
    print("y1:", Object.get_points()[0][1])
    print(cal_coord)
    dist = process.pixeldistance(cal_coord[0][0], cal_coord[0][1], cal_coord[1][0], cal_coord[1][1])
    Object.set_measurement(dist)
    print("Distance between points:", Object.get_measurement())
    # Michael will put user interface to collect real-world distance
    guiObject.DistanceInput()
    the_dist = guiObject.get_distance()
    print("Entered Distance:", the_dist)
    Object.set_real_dist(100)
    
def butt_connect():
    cv2.imread(image_path)
    guiObject.pages.setCurrentIndex(1)
    calibrate_system(imageObject)

if __name__ == '__main__':
    # image = cv2.imread(image_path)
    # calibrate_system(imageObject)
    guiObject.set_start_button(butt_connect)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    sys.exit(app.exec_()) # execute app