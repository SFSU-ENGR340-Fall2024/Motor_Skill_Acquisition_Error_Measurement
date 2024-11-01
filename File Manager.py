
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

    def _init_(self):
        self.current_directory = os.path.dirname(os.path.abspath(__file__))
        print("Current directory:", self.current_directory)
    
        #File attribute 
        
    
#Folder methods 
    
    "Works"
    #Creates folder that for the results 
    def CreateFolder():
        os.makedirs("results", exist_ok=True)
        print("Folder has been created")

    "Works"
    #Open selected folder in the selected directory 
    def OpenFolder():
        current_directory = os.path.dirname(os.path.abspath(__file__))
        os.startfile(current_directory)  

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

    "Works but wanted to put into results folder"
    #Create File (This is the results file)
        #Get Folder directory
    def CreateFile():
        filename = 'results.txt' 

        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_name = "results.csv"

        file_path = os.path.join(current_directory, file_name)

        with open(file_path, 'w') as file:
            file.write("X coordinates: " + "\n")       
            file.write("Y coordinates: ")


    #Load file 
        #Get Folder directory 
        #Get File name 
        #Load File 
    def LoadFile():
        
        #Finds file in directory
        file_path = os.path.join(current_directory, filename)
    
        with open(file_path, 'r') as file:
                content = file.read()  # Read the entire file


    #Copy Files
        #Get Folder directory 
        #Get File name 
        #Copy file date 
    def CopyFile(self):

        # Define the source file path (in the current directory)
        source_file = os.path.join(os.getcwd(), file_name)

        # Define the destination file path (in the same directory, but with a different name)
        destination_file = os.path.join(os.getcwd(), 'copy_of_' + filename + '.txt')

        # Copy the file
        shutil.copy(source_file, destination_file)

    #Delete File 
        #Get Folder directory 
        #Get File name 
    def DeleteFile(self):

        # Delete the file if it exists
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"{file_name} has been deleted from the current directory.")
        else:
            print(f"{file_name} does not exist in the current directory.")


    #Change File Location
        #Get directory of current folder
        #Get selected file 
        #Get directory of selected folder
        #Copy File
        #Paste File 

    #Put File in certain directory (Image file to directory)
              
              
              
if __name__ == "__main__":
    FileManager.CreateFile()

