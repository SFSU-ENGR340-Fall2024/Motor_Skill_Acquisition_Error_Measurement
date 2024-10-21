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

    #Change Folder Location        


#File methods

    #Create File

    #Load file 

    #Copy Files 

    #Delete File 

    #Move File

    #Change File Location 
              
if __name__ == '__main__':
    print(CreateFolder())


