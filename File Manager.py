''' 
File management

This should create a folder within the selected folder with
results 

 '''
import os
import shutil 

class FileManager:
     
    # Our Folder location as our attribute
    # Get the directory of the current file (Python file must be in folder with images)
    current_directory = os.path.dirname(os.path.abspath(__file__))
    print("Current directory:", current_directory)
    
    #File attribute 
    filepath 

    
#Folder methods 
    
    #Creates folder 
    #Note: Needs object 
    def CreateFolder(self):
        if not os.path.exists("path/to/demo_folder"): 
              os.makedirs("path/to/demo_folder")

    #Deletes folder 
        #Get directory 
        #Select folder 

        #Deletes folder and it's content 
    def DeleteFolder(self, current_directory):
    # Delete the directory (only works if the directory is empty)
        try:
            shutil.rmtree(current_directory)
            print(f"Successfully deleted the directory and its contents: {directory}")
        except OSError as e:
            print(f"Error: {e.strerror}")



    #Change Folder Location
        #Get directory of current folder
        #Get directory of selected folder 
        

#File methods

    #Create File (This is the results file)
        #Get Folder directory
    def CreateFile(self):
        filename = 'results.txt' 

        with open(filename, 'w') as file:
            file.write("X coordinates: " + "\n")       
            file.write("Y coordinates: ")

    #Load file 
        #Get Folder directory 
        #Get File name 
        #Load File 
    def LoadFile(self, filename, current_directory):
        
        #Finds file in directory
        file_path = os.path.join(current_directory, filename)
    
        with open(file_path, 'r') as file:
                content = file.read()  # Read the entire file

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


