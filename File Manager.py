''' 
File management

This should create a folder within the selected folder with
results 

 '''
import os 

class FileManager:
    
    #Need to create folder object 
    
    # Our Folder location as our attribute
    # Get the directory of the current file (Python file must be in folder with images)
    current_directory = os.path.dirname(os.path.abspath(__file__))
    print("Current directory:", current_directory)
    
    
#Folder methods 
    
    #Creates folder 
    #Note: Needs object 
    def CreateFolder(self):
        if not os.path.exists("path/to/demo_folder"): 
              os.makedirs("path/to/demo_folder")

    #Deletes folder 
        #Get directory 
        #Select folder 
        #Deletes folder 

    #Change Folder Location
        #Get directory of current folder
        #Get directory of selected folder 
        

#File methods

    #Create File
        #Get Folder directory
            #Conditional for checking if file is created
            #False if not there
            #True if there
        #Creates file 

    #Load file 
        #Get Folder directory 
        #Get File name 
        #Load File 

    #Copy Files
        #Get Folder directory 
        #Get File name 
        #Copy file date 

    #Delete File 
        #Get Folder directory 
        #Get File name 
        #Copy file date 

    #Move File
        #Get Folder directory 
        #Get File name 
        #Copy file date 

    #Change File Location
        #Get directory of current folder
        #Get selected file 
        #Get directory of selected folder
        #Copy File
        #Paste File 
              
              
              
if __name__ == '__main__':
    print(CreateFolder())


