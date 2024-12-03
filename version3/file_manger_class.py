import os

class FileManager:
    def __init__(self):
        self.created_folders = set()  # Initialize the set to track created folders

    def create_folder(self, folder_path, folder_name="Results"):
        """
        Create a folder named `folder_name` in the specified folder location (`folder_path`).
        Only creates the folder if it does not already exist.
        Returns the full path to the folder.
        """
        target_path = os.path.join(folder_path, folder_name)
        if target_path not in self.created_folders and not os.path.exists(target_path):
            os.makedirs(target_path, exist_ok=True)
            self.created_folders.add(target_path)
            print(f"Folder '{folder_name}' has been created at: {target_path}")
        else:
            print(f"Folder '{folder_name}' already exists at: {target_path}")
        return target_path  # Return the path whether it was newly created or already existed

    def create_text_file(self, folder_path, file_name="ResultTextFile.txt", content=""):
        """
        Create a text file in the specified folder.
        
        Args:
            folder_path (str): The path to the folder where the file should be created.
            file_name (str): The name of the text file to create (default: "output.txt").
            content (str): Optional content to write to the file (default: empty string).
        
        Returns:
            str: The full path to the created file.
        """
        # Ensure the folder exists
        if not os.path.exists(folder_path):
            print(f"Folder '{folder_path}' does not exist. Creating the folder.")
            os.makedirs(folder_path, exist_ok=True)

        # Define the full file path
        file_path = os.path.join(folder_path, file_name)

        # Create and write to the file
        with open(file_path, "w") as file:
            file.write(content)
            print(f"File '{file_name}' has been created at: {file_path}")

        return file_path  # Return the path to the created file


    def append_to_text_file(self, file_path, content=""):
        """
        Append content to a text file at the specified file path.
        If the file does not exist, it will be created.

        Args:
            file_path (str): The full path to the text file.
            content (str): The content to append to the file.

        Returns:
            None
        """
        # Ensure the folder containing the file exists
        folder_path = os.path.dirname(file_path)
        if not os.path.exists(folder_path):
            print(f"Folder '{folder_path}' does not exist. Creating the folder.")
            os.makedirs(folder_path, exist_ok=True)

        # Append content to the file
        with open(file_path, "a") as file:  # Open in append mode
            file.write(content)
            print(f"Appended content to file at: {file_path}")