''' 
File management

This should create a folder within the selected folder with
results 

 '''
import os
from datetime import datetime
import shutil
from PyQt5.QtWidgets import QFileDialog

class FileManager:
     
    # Our Folder location as our attribute
    # Get the directory of the current file (Python file must be in folder with images)

    def __init__(self):
        self.current_directory = os.path.dirname(os.path.abspath(__file__))
        print("Current directory:", self.current_directory)
    
        #File attribute 
        
    
#Folder methods 
    
    "Works"
    #Creates folder that for the results 
    def create_folder(self, folder_path, folder_name="Results"):
        """
        Create a folder named `folder_name` in the specified folder location (`folder_path`).
        Returns the full path to the created folder.
        """
        target_path = os.path.join(folder_path, folder_name)
        os.makedirs(target_path, exist_ok=True)
        print(f"Folder '{folder_name}' has been created at: {target_path}")
        return target_path  # Ensure the path string is returned
    def create_txt_file(self, folder_path, filename="results.txt"):
        """
        Create a text file named `filename` in the specified folder path.

        :param folder_path: Path to the folder where the file will be created.
        :param filename: Name of the text file to create.
        """
        # Construct the full path for the text file
        file_path = os.path.join(folder_path, filename)

        # Get the current date and time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Create and write content to the text file
        with open(file_path, 'w') as file:
            file.write(f"Results Last Edit: {current_time}\n")

        print(f"Text file '{filename}' has been created at: {file_path}")
        return file_path  # Return the path of the created text file
    
      


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

    #Getter for folder 
    def get_folder(self):
        return self.__folder
    
    #Setter for folder
    def set_folder(self):
        self.__folder = QFileDialog.getExistingDirectory(self, 'Select Folder')
        return self.__folder
    
    #Select Folder function 
    def select_folder(self):
        self.set_folder()
        return self.label.setText(self.get_folder())

    #Change Folder Location
        #Get directory of current folder
        #Get directory of selected folder 


#File methods

    "Works but wanted to put into results folder"
    #Create text file called "results.txt"
    

    # Add Results to text file in same row then add new line 

    def edittext(self,textfile,Idx, realdistance, xvalues, yvalues, puckpoints, centerpoints ):
        """
        Append labeled results to a text file in the same row, then add a new line.

        :param textfile: Path to the text file to edit.
        :param Idx: Index or identifier of the data entry.
        :param realdistance: The real distance measurement.
        :param xvalues: List of x-coordinates.
        :param yvalues: List of y-coordinates.
        :param puckpoints: Coordinates of puck points.
        :param centerpoints: Coordinates of center points.
        """
        # Open the text file in append mode
        with open(textfile, 'a') as file:
            # Write the labeled data in a single row
            file.write(
                f"Index: {Idx}, "
                f"Real Distance: {realdistance}, "
                f"X Values: {xvalues}, "
                f"Y Values: {yvalues}, "
                f"Puck Points: {puckpoints}, "
                f"Center Points: {centerpoints}\n")

       
       
    
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
    pass

    #Open folder directory
    #FileManager.OpenFolder()

    #Creates results folder 
    #FileManager.CreateFolder()

    #Creates txt file 
    #FileManager.CreateTxtFile()

    #Creates csv file 
    #FileManager.CreateCSVFile()

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