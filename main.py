#Main file for the motor skills aquisition error measurment project


#imports
import sys
import os
from PyQt5.QtWidgets import QApplication

#class imports
from Image_Data import Image_Data
from GUI.gui import GUI
# from GUI.gui import Start
#from ImageProcces.ImageprocessClass import Imageproccess

#Main
if __name__ == '__main__':
    #PSEUDOCODE:
        #GUI Home
        #IF image processing
            #GUI Image Display
            #IF change folder
                #select new folder
            #IF results folder found
                #tell the user
            #GUI Calibration
            #Calibration
            #IF restart calibration
                #Calibration again
            #GUI Error Calculation

    #start
    print('start')
    #init error calc, file handler
    #ip = Imageproccess()
    #Display Home GUI and init the GUI object
    app = QApplication(sys.argv)
    g = GUI()
    #IF image processing
    if g.last_button == 'Image Processing':
        #Display image display GUI

        #IF user rejects folder
        if g.last_button == 'Reject Folder':
            pass
            #Allow user to select new folder
            
        #IF user accepts folder
        if g.last_button == "Accept Folder":
            #get the selected folder
            folder = g.get_folder()
            #check every file/folder in directory
            for i in os.listdir(folder):
                #IF the results folder is found
                if i == folder + "_results":
                    #tell the user, do something else?
                    print("There is already results for this data")
            #Display image processing GUI
            
            #init calibration_finished to false
            calibration_finished = False
            #while the calibration is not accepted
            while calibration_finished == False:
                #Initial calibration UI

                #wait for the calibration image to be selected
                if g.last_button == "Calibration Image Selection":
                    #Get the calibration image
                    calibration_image = g.get_calibration_image()
                    #run the calibration on the image

                    #show UI with calibration data

                #if user accepts calibration
                if g.last_button == "Accept Calibration":
                    calibration_finished = True
                    
            #make an empty array to store all the image_data
            image_data_array = []
            image_extesions = ('.png', '.jpg', '.jpeg')
            #for everything in the folder
            for i in os.listdir(folder):
                #if the item is an image, but not the calibration image
                if i.lower().endswith(image_extesions) and i != calibration_image:
                        #make an image_data object for the item and append to array
                        image_data_array.append(Image_Data(i))
            #show the image_processing GUI
            
            #init image_process_finished to false
            image_process_finished = False
            #init the image_data_array_counter to the length of array - 1
            max_count = len(image_data_array) - 1
            count = 0
            #while the image_process is not finished
            while image_process_finished == False:
                #load an image into the GUI
                pass
                


            #make Image_Data obj for every image in folder but calibration image
            #display image for processing
            #have user click on puck
            #calculate error and related info
            #display info to user
            #IF user does not like info
                #Allow user to move clicks
            #User confirms info is correct
            #Display next image, repeat process until done
    
    #IF show results
    if g.last_button == 'Results':
        #get the selected folder
        folder = g.get_folder()
        #User selects a folder

    sys.exit(app.exec_())
    print(g.get_folder())