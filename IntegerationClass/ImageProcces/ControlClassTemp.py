import sys, cv2
import numpy as np
from classtest import classtest
from DataClassTemp import DataClass
from ImageProcces import ImageProcess

ImageDisplayWidth = 1500
ImageDisplayHeight = 700
image_path = r'C:\Users\milto\OneDrive\Desktop\ImagineProcessClass\Motor_Skill_Acquisition_Error_Measurement\IntegerationClass\ImageProcces\RulerPicture.jpg'

guiObject = classtest()
imageObject = DataClass(image_path, ImageDisplayWidth, ImageDisplayHeight)
process = ImageProcess()

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
    


    

if __name__ == '__main__':
    calibrate_system(imageObject)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    