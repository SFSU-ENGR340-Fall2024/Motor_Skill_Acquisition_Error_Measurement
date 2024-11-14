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
image_path = "C:/Users/milto/OneDrive/Desktop/340FinalProject/Motor_Skill_Acquisition_Error_Measurement/IntegerationClass/ImageProcces/RulerPicture.jpg"

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
    Object.set_scaling_factor(process.scalingfactor(Object.get_real_dist(), Object.get_measurement())) 

def image_reset(Object):
    # Restart the image to original
    cv2.destroyAllWindows() 
    Object.set_resized_image(Object.get_original_image())
    Object.set_image(Object.get_original_image())
    cv2.waitKey(1)  # Optional, but ensures smoothness in some environments
    cv2.destroyAllWindows() 


def first_error_measurement(Object):
    # Restart the image to original
    image_reset(Object)
    # Collection of points for center and puck
    imageObject.set_center(guiObject.center_point_collection(Object.get_resized_image()))
    image_reset(Object)
    imageObject.set_puck(guiObject.puck_point_collection(Object.get_resized_image()))
    # calculate the real-world distance between the two points
    Object.set_error_measurement_value(process.errorcalculationxy(Object.get_center()[0][0], Object.get_center()[0][1], Object.get_puck()[0][0], Object.get_puck()[0][1], Object.get_scaling_factor()))

def error_measurement(Object):
    imageObject.set_puck(guiObject.puck_point_collection(Object.get_resized_image()))
    
def butt_connect():
    cv2.imread(image_path)
    guiObject.pages.setCurrentIndex(1)
    calibrate_system(imageObject)
    error_measurement(imageObject)
    first_error_measurement(imageObject)

if __name__ == '__main__':
    guiObject.set_start_button(butt_connect)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    sys.exit(app.exec_()) # execute app
  