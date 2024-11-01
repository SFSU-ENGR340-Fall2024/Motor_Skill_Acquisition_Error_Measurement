import sys
import cv2
import numpy as np
from classtest import classtest
from DataClassTemp import DataClass

ImageDisplayWidth = 1500
ImageDisplayHeight = 700
image_path = r'C:\Users\milto\OneDrive\Desktop\ImagineProcessClass\Motor_Skill_Acquisition_Error_Measurement\IntegerationClass\ImageProcces\RulerPicture.jpg'

guiObject = classtest()
imageObject = DataClass(image_path, ImageDisplayWidth, ImageDisplayHeight)

def calibrate_system(Object):
    # Collection of points for calibration
    guiObject.calibration_point_collection(Object.get_resized_image())
    print("Calibration points:", Object.get_points())
    

if __name__ == '__main__':
    calibrate_system(imageObject)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    