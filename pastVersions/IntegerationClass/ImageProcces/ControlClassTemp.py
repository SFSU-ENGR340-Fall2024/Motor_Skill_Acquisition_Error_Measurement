import sys, cv2
import numpy as np
from classtest import classtest
from DataClassTemp import DataClass
from ImageProcces import ImageProcess
from GUICopy import GUI
from test import Test2
from PyQt5.QtWidgets import QApplication
import os
from PIL import Image
from File_Manager import FileManager

ImageDisplayWidth = 1500
ImageDisplayHeight = 700
image_path = None

manager = FileManager() 
app = QApplication(sys.argv) # create application object
guiObject = GUI()
process = ImageProcess()
testPage = Test2()
the_dist = None
image_objects = []
textfile =  None; 

def calibrate_system(Object):
    # Collection of points for calibration
    Object.set_points(guiObject.calibration_point_collection(Object.get_resized_image()))
    cal_coord = Object.get_points()
    dist = process.pixeldistance(cal_coord[0][0], cal_coord[0][1], cal_coord[1][0], cal_coord[1][1])
    Object.set_measurement(dist)
    guiObject.setMeasurement(dist)
    guiObject.DistanceInput()
    the_dist = guiObject.setDistance()
    guiObject.updatePage2Labels()
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
    Object.set_center(guiObject.center_point_collection(Object.get_resized_image()))
    # print center point
    print(Object.get_center())
    image_reset(Object)
    Object.set_puck(guiObject.puck_point_collection(Object.get_resized_image()))
    # calculate the real-world distance between the two points
    Object.set_error_measurement_value(process.errorcalculationxy(Object.get_center()[0][0], Object.get_center()[0][1], Object.get_puck()[0][0],
                                                                  Object.get_puck()[0][1], Object.get_scaling_factor()))

def error_measurement(Object):
    Object.set_puck(guiObject.puck_point_collection(Object.get_resized_image()))
     # calculate the real-world distance between the two points
    Object.set_error_measurement_value(process.errorcalculationxy(Object.get_center()[0][0], Object.get_center()[0][1], Object.get_puck()[0][0],
                                                                  Object.get_puck()[0][1], Object.get_scaling_factor()))
    
def butt_connect():
    if guiObject.get_folder() is None:
        print("No folder")
    else:
        # Set the current page to the second page
        guiObject.pages.setCurrentIndex(1)

        # Have the user select the calibration image
        guiObject.set_image()
        image_path = guiObject.get_image()

        # Save the folder path and create a list of images in the folder
        folder_path = guiObject.get_folder()
        imagelist = sorted([f for f in os.listdir(folder_path) if f.endswith(('.png', '.JPG', '.jpeg'))])

       # Create Folder in ImageData
        resultFolder = manager.create_folder(folder_path, "Results")  # This will return the path to the "Results" folder

        # Create a text file to store the results
        textfilepath = manager.create_txt_file(resultFolder)  # Pass the correct path string to CreateTxtFile
        # edittext(textfile,Idx, realdistance, xvalues, yvalues, puckpoints, centerpoints ):
       

        # Ensure the calibration image is the first in the list
        calibration_image_name = os.path.basename(image_path)  # Extract the file name of the selected image
        if calibration_image_name in imagelist:
            imagelist.remove(calibration_image_name)  # Remove it from its current position
            imagelist.insert(0, calibration_image_name)  # Insert it at the start

        # Create the first image object (calibration image) and calibrate the system
        calibration_image_path = os.path.join(folder_path, imagelist[0])  # Full path of the calibration image
        calibration_object = DataClass(calibration_image_path, ImageDisplayWidth, ImageDisplayHeight)
        calibrate_system(calibration_object)
        image_objects.append(calibration_object)

        # Perform first error measurement on the second image
        second_image_path = os.path.join(folder_path, imagelist[1])  # Full path of the second image
        second_image_object = DataClass(second_image_path, ImageDisplayWidth, ImageDisplayHeight)
        second_image_object.set_scaling_factor(calibration_object.get_scaling_factor())
        first_error_measurement(second_image_object)
        image_objects.append(second_image_object)
        # Save information to text file
        # edittext(textfile,Idx, realdistance, xvalues, yvalues, puckpoints, centerpoints ):
        manager.edittext(textfilepath, 1, second_image_object.get_error_measurement_value(),second_image_object.get_diff_x(), second_image_object.get_diff_y(), second_image_object.get_puck(), second_image_object.get_center())

        
        # Store calibration values for reuse
        center = second_image_object.get_center()
        scaling_factor = second_image_object.get_scaling_factor()
        real_dist = second_image_object.get_real_dist()
        measurement = second_image_object.get_measurement()
        points_calibration = second_image_object.get_points()

        # Process the rest of the images in the list (starting from the third image)
        for idx, image_name in enumerate(imagelist[2:], start=2):
            image_path = os.path.join(folder_path, image_name)
            other_image_object = DataClass(image_path, ImageDisplayWidth, ImageDisplayHeight)

            # Apply calibration values to the current image
            other_image_object.set_center(center)
            other_image_object.set_scaling_factor(scaling_factor)
            other_image_object.set_real_dist(real_dist)
            other_image_object.set_measurement(measurement)
            other_image_object.set_points(points_calibration)

            # Append the other image object to the list
            image_objects.append(other_image_object)

        # Initialize the image navigation
        i = 2 # Start with the second image (first processed image)
        back = False

        while True:

            # Automatically process the current image
            error_measurement(image_objects[i])
            # Save information to text file
            manager.edittext(textfilepath, i, image_objects[i].get_error_measurement_value(), image_objects[i].get_diff_x(), image_objects[i].get_diff_y(), image_objects[i].get_puck(), image_objects[i].get_center())
            # Determine navigation direction
            if back:
                i -= 1
                if i < 1:  # Prevent going below the second image
                    i = 1
                    back = False
            else:
                i += 1
                if i >= len(image_objects):  # Exit the loop after processing all images
                    print("All images processed.")
                    break
        
if __name__ == '__main__':
    guiObject.set_start_button(butt_connect)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    sys.exit(app.exec_()) # execute app
  