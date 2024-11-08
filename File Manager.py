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
        os.makedirs("Results", exist_ok=True)
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
    #Create text file called "results.txt"
    def CreateTxtFile():

        #Get the current directory for
        current_directory = os.path.dirname(os.path.abspath(__file__))

        # File type that will be created 
        file_name = "results.txt"

        file_path = os.path.join(current_directory, file_name)

        with open(file_path, 'w') as file:
            file.write("X coordinates: " + "\n")       
            file.write("Y coordinates: ")
    
    "Works"
    #Creates cvsfile called "results.csv"
    def CreateCSVFile():

        #Get the current directory for
        current_directory = os.path.dirname(os.path.abspath(__file__))

        # File type that will be created 
        file_name = "results.csv"

        file_path = os.path.join(current_directory, file_name)

        with open(file_path, 'w') as file:
            file.write("X coordinates: " + "\n")       
            file.write("Y coordinates: ")
    
    "Works"
    #Create excel file called "results.xlsx"
    def CreateXLSXFile():

        #Get the current directory for
        current_directory = os.path.dirname(os.path.abspath(__file__))

        # File type that will be created 
        file_name = "results.xlsx"

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
    def DeleteFile():

        # Delete the file if it exists
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"{file_name} has been deleted from the current directory.")
        else:
            print(f"{file_name} does not exist in the current directory.")

    "Works"
    #Put File in certain directory (Image file to directory)
    def FileRelocation(filename):

        # Gets the current directory 
        current_directory = os.path.dirname(os.path.abspath(__file__))

        # Source file to move (Note you need to add file exten type)
        file_to_move = filename
    
        """
        Try to move other the 
        txt     -Works
        excel   -Works
        csv     -Works
        2 images
        (Jpg, Jpeg, PNG) -Works
        ("results.txt","results.csv","results.xlsx")
        
        """

        # Destination folder for the file to move to 
        destination_folder = "ResultsFolder"

        # Construct the full paths for the source and destination   
        source_path = os.path.join(current_directory, file_to_move)
        destination_path = os.path.join(current_directory, destination_folder, file_to_move)

        # Move the file
        shutil.move(source_path, destination_path)
              
              
              
if __name__ == "__main__":

    #Open folder directory
    #FileManager.OpenFolder()

    #Creates results folder 
    #FileManager.CreateFolder()

    #Creates txt file 
    #FileManager.CreateTxtFile()

    #Creates csv file 
    FileManager.CreateCSVFile()

    #Creates excel file
    #FileManager.CreateXLSXFile()
    
    """
    #Relocate each file to results folder 
        #Text file 
    FileManager.FileRelocation("results.txt")
        #CSV File 
    FileManager.FileRelocation("results.csv")
        #XLSX File
    FileManager.FileRelocation("results.xlsx") 
    """