#Main file for the motor skills aquisition error measurment project


#imports
import sys
from PyQt5.QtWidgets import QApplication

#class imports
# from Image_Data import Image_Data
from GUI.gui import GUI
from GUI.gui import Start
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

    #Display Home GUI
    app = QApplication(sys.argv)
    g = GUI()
    folder = g.get_folder()
    button = g.last_button
    
    if button == 'Select Folder':
        print(folder)

    #IF image processing
    if g.last_button == 'Image Processing':
        #get the selected folder
        folder = g.get_folder()
        #Display image display GUI

        #error check
        if g.last_button != 'Reject Folder' and g.last_button != 'Accept Folder':
            print('Error with folder selection')
        #IF user rejects folder
        if g.last_button == 'Reject Folder':
            pass
            #Allow user to select new folder
                
        #IF user accepts folder
        if g.last_button == "Accept Folder":
            pass
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
    if g.last_button == 'Results':
        #get the selected folder
        folder = g.get_folder()
        #User selects a folder

    sys.exit(app.exec_())
    print(g.get_folder())