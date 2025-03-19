
############################################################################################
# Project Name: Motor Skill Acquisition Error Management System (San Francisco State University Project 2024) 
# 
# Filename: file_manager_class.py
# 
# Authors: Milton Tinoco, Ethan Weldon, Joshua Samson, Michael Cabrera
#
# Last Update: 12/08/2024
#
# File Description:
#
# This file contains the code for file management, which creates folders and text files, appends data to files, and removes the last line from a file.
#
#
############################################################################################

# Import necessary libraries
import os

# Class: FileManager
# Description: This class provides methods to create folders, text files, 
#              append data to files, and remove the last line from a file.

class FileManager:
    def __init__(self):
        self.created_folders = set()  # Track created folders

    def create_folder(self, folder_path, folder_name="Results"):
        """
        Description: Create a folder if it doesn't exist and return the path.
        Input: folder_path - Path to the folder where the new folder should be created
               folder_name - Name of the new folder (default: "Results")
        Output: target_path - Path to the created folder
        """
        target_path = os.path.join(folder_path, folder_name)
        if target_path not in self.created_folders and not os.path.exists(target_path):
            os.makedirs(target_path, exist_ok=True)
            self.created_folders.add(target_path)
        return target_path
    
    def create_text_file(self, folder_path, file_name="Results_File.txt", content=""):
        """
        Description: Create a text file if it doesn't exist and optionally write content.
        Input: folder_path - Path to the folder where the file should be created
               file_name - Name of the text file (default: "Results_File.txt")
               content - Content to write to the file (default: "")
        Output: file_path - Path to the created text file
        """
        if not os.path.exists(folder_path):
           
            os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, file_name)
        if not os.path.exists(file_path):
            with open(file_path, "w") as file:
                file.write(content)
        return file_path
    
    def append_axis_data(self, file_path, image_index, radial, yaxis, xaxis):
        """
        Description: Append axis data to a text file.
        Input: file_path - Path to the text file
               image_index - Index of the image trial
               radial - Radial value
               yaxis - Y-axis value
               xaxis - X-axis value
        Output: None
        """
        if not os.path.exists(file_path):
            with open(file_path, "w") as file:
                # Header with column names
                file.write(f"{'Image Index':<15}{'Radial':<15}{'X-Axis':<15}{'Y-Axis':<15}\n")
                file.write("=" * 60 + "\n")  # Separator line

        with open(file_path, "a") as file:
            # Append the data with labels
            # 'No Trial' button pressed, append 'N/A'
            if all(type(data) == str for data in (radial, yaxis, xaxis)):
                file.write(f"Image Trial: {image_index:<10} Radial: {radial} \t\t X-Axis: {xaxis}\t Y-Axis: {yaxis}\n")
            # Valid test image click or 'Out of Bounds" button clicked, append data
            else:
                file.write(f"Image Trial: {image_index:<10} Radial: {radial:<10.2f} X-Axis: {xaxis:<10.2f} Y-Axis: {yaxis:<10.2f}\n")
    
    def remove_last_line(self, file_path):
        """
        Description: Remove the last line from the file.
        Input: file_path - Path to the file where the last line should be removed
        Output: None
        """
        with open(file_path, "r") as file:
            lines = file.readlines()

        if len(lines) > 1:  # Ensure there's something to remove (excluding the header)
            with open(file_path, "w") as file:
                file.writelines(lines[:-1])  # Write all lines except the last one
           
