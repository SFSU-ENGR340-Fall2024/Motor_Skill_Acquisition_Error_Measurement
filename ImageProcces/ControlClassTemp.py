from MeasurmentClass import ImageProcess
from DataClassTemp import DataClass
import cv2

ImageDisplayWidth = 800
ImageDisplayHeight = 600
image_path = r'C:\Users\milto\OneDrive\Desktop\ImagineProcessClass\.venv\data\RulerPicture.jpg'
nextimage = r'C:\Users\milto\OneDrive\Desktop\ImagineProcessClass\.venv\data\IMG_1687.JPG'

data_instances = [] # Create a list to store the data instances
data_instance = DataClass(image_path) # Create a data instance
data_instances.append(data_instance) # Append the data instance to the list

# Create a measurement instance
measurement_instance = ImageProcess(data_instances)


