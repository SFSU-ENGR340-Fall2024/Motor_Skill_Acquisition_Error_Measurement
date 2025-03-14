import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class ImageViewer:
    def __init__(self):
        print("Current Working Directory:", os.getcwd())
        self.image_folder = os.path.join(os.getcwd(), "programImages")  # Ensure this matches your actual folder name
        self.image_files = ["graph1.png", "graph2.png", "graph3.png", "graph4.png"]
        self.current_index = 0  # Start at the first image

    def show_image(self):
        print(f"Looking in folder: {self.image_folder}")

        # Check if folder exists
        if not os.path.exists(self.image_folder):
            print(f"Error: Folder '{self.image_folder}' does not exist.")
            return

        # Print available files in folder
        available_files = os.listdir(self.image_folder)
        print("Available files in folder:", available_files)

        if not self.image_files:
            print("No images to display.")
            return

        image_path = os.path.join(self.image_folder, self.image_files[self.current_index])

        if not os.path.exists(image_path):
            print(f"Error: Image not found: {image_path}")
            return

        print(f"Displaying: {self.image_files[self.current_index]}")
        
        img = mpimg.imread(image_path)
        plt.imshow(img)
        plt.axis("off")
        plt.title(self.image_files[self.current_index])
        plt.show()

# Example usage
viewer = ImageViewer()
viewer.show_image()
