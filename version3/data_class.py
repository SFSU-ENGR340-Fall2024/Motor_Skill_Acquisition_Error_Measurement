import cv2

# Object created based on each image in the folder used for calibration
class DataClass:
    ############################################################
    # Constructor for the DataClass 
    ############################################################


    def __init__(self, image):
        ############################################################
        # Attributes for the DataClass class
        ############################################################
        # Store the image relate to the object
        self.image = cv2.imread(image)
        # Store the two point used for caculation
        self.points = []
        # Calibration distance between the two points in pixels 
        self.calibration_pixels_distance = None
        # Real life distance between the two points 
        self.real_distance_measurement = None
        # Store the scaling factor from  real distance divivby calibration distance
        self.scaling_factor = None
        # Store the list of images in the folder
        self.image_list=[]
        # Store the postiion this object is in the list
        self.position_index = None
        # Store the real world differnece in x direction between the puck and the center 
        self.real_world_x_diff = None
        # Store the real world differnece in y direction between the puck and the center
        self.real_world_y_diff = None
        # Store the real world distance between the puck and the center
        self.real_world_distance = None
        # Store the real world percentage of the distance between the puck and the center
        self.real_world_percentage = None
        # Store the file path location of results
        self.results_file_path = None
    
    
    ############################################################
    # Getter and Setter methods for the DataClass class 
    ############################################################
    
    # Setter methods #

    # Set the file path location of results
    # Input: results_file_path - the file path location of results
    # Output: None
    def set_results_file_path(self, results_file_path):
        self.results_file_path = results_file_path

    # set the two point used for caculation
    # Input: point - the two point used for caculation
    # Output: None
    def set_points(self, points):
        self.points = points

    

    # Set the real world percentage of the distance between the puck and the center
    # Input: real_world_percentage - the real world percentage of the distance between the puck and the center
    # Output: None
    def set_real_world_percentage(self, real_world_percentage):
        self.real_world_percentage = real_world_percentage
    
    # Set the real world distance between the puck and the center
    # Input: real_world_distance - the real world distance between the puck and the center
    # Output: None
    def set_real_world_distance(self, real_world_distance):
        self.real_world_distance = real_world_distance
    
    # Set the real world differnece in y direction between the puck and the center
    # Input: real_world_y_diff - the real world differnece in y direction between the puck and the center
    # Output: None
    def set_real_world_y_diff(self, real_world_y_diff):
        self.real_world_y_diff = real_world_y_diff
    
    # Set the real world differnece in x direction between the puck and the center
    # Input: real_world_x_diff - the real world differnece in x direction between the puck and the center
    # Output: None
    def set_real_world_x_diff(self, real_world_x_diff):
        self.real_world_x_diff = real_world_x_diff

    # Set the list of images in the folder
    # Input: image_list - the list of images in the folder
    # Output: None
    def set_image_list(self, image_list):
        self.image_list = image_list

    # Set the position index of the object in the list
    # Input: position_index - the position index of the object in the list
    # Output: None
    def set_position_index(self, position_index):
        self.position_index = position_index

    # Set the image attribute of the object
    # Input: image - the image to be set
    # Output: None
    def set_image(self, image):
        self.image = cv2.imread(image)
    
    # Set the calibration distance between the two points in pixels
    # Input: calibration_pixels_distance - the calibration distance between the two points in pixels
    # Output: None
    def set_calibration_pixels_distance(self, calibration_pixels_distance):
        self.calibration_pixels_distance = calibration_pixels_distance
    
    # Set the real life distance between the two points
    # Input: real_distance_measurement - the real life distance between the two points
    # Output: None
    def set_real_distance_measurement(self, real_distance_measurement):
        self.real_distance_measurement = real_distance_measurement
    
    # Set the scaling factor from  real distance divivby calibration distanc
    # Input: scaling_factor - the scaling factor from  real distance divivby calibration distance
    # Output: None
    def set_scaling_factor(self, scaling_factor):
        self.scaling_factor = scaling_factor

    # Getter methods #

    # Get the file path location of results
    # Input: None
    # Output: results_file_path - the file path location of results
    def get_results_file_path(self):
        return self.results_file_path

    # Get the two point used for caculation
    # Input: None
    # Output: point - the two point used for caculation
    def get_points(self):
        return self.points
    

    # Get the real world percentage of the distance between the puck and the center
    # Input: None
    # Output: real_world_percentage - the real world percentage of the distance between the puck and the center
    def get_real_world_percentage(self):
        return self.real_world_percentage
    
    # Get the real world distance between the puck and the center
    # Input: None
    # Output: real_world_distance - the real world distance between the puck and the center
    def get_real_world_distance(self):
        return self.real_world_distance
    
    # Get the real world differnece in y direction between the puck and the center
    # Input: None
    # Output: real_world_y_diff - the real world differnece in y direction between the puck and the center
    def get_real_world_y_diff(self):
        return self.real_world_y_diff
    
    # Get the real world differnece in x direction between the puck and the center
    # Input: None
    # Output: real_world_x_diff - the real world differnece in x direction between the puck and the center
    def get_real_world_x_diff(self):
        return self.real_world_x_diff
    
    # Get the list of images in the folder
    # Input: None
    # Output: image_list - the list of images in the folder
    def get_image_list(self):
        return self.image_list
    
    # Get the position index of the object in the list
    # Input: None
    # Output: position_index - the position index of the object in the list
    def get_position_index(self):
        return self.position_index
    
    # Get the image attribute of the object
    # Input: None
    # Output: image - the image attribute of the object
    def get_image(self):
        return self.image
    
    # Get the calibration distance between the two points in pixels\
    # Input: None
    # Output: calibration_pixels_distance - the calibration distance between the two points in pixels
    def get_calibration_pixels_distance(self):
        return self.calibration_pixels_distance
    
    # Get the real life distance between the two points
    # Input: None
    # Output: real_distance_measurement - the real life distance between the two points
    def get_real_distance_measurement(self):
        return self.real_distance_measurement
    

    # Get the scaling factor from  real distance divivby calibration distanc
    # Input: None
    # Output: scaling_factor - the scaling factor from  real distance divivby calibration distance
    def get_scaling_factor(self):
        return self.scaling_factor
    

    ############################################################

    

        
    





    