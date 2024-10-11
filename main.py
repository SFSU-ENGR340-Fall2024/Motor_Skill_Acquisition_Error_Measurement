#Main file for the motor skills aquisition error measurment project


#imports
import sys
from PyQt5.QtWidgets import QApplication

#class imports
from Image_Data import Image_Data
from GUI.gui import GUI

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

    #Display Home GUI
    #IF image processing
        #User selects a folder
        #Display image display GUI
        #IF user rejects folder
            #Allow user to select new folder
        #IF user accepts folder
            #IF results fodler is found
                #tell the user, do something else?
            #Display image processing GUI
            #User selects calibration image
            #Calibration process
            #IF user rejects calibration
                #redo clibration
            #User accepts calibration
            #make Image_Data obj for every image in folder but calibration image
            #display image for processing
            #have user click on puck
            #calculate error and related info
            #display info to user
            #IF user does not like info
                #Allow user to moce clicks
            #User confirms info is correct
            #Display next image, repeat process until done


            

    #IF show results
        #User selects a folder