
import cv2


class DataClass:
    def __init__(self, image, width=1500, height=700):
    # This store the image
        self.image = image 
        # This store the resized image
        self.imageresized = cv2.resize(self.image, (width, height))
        # Store a copy of the original image to allow resetting to its initial state.
        # Modifications made to the image are applied directly and remain permanent.
        self.original_image = self.imageresized.copy() 
        # This store calibration points 
        self.points = [] 
        # This store the scaling factor for calibration
        self.scaling_factor = None
        # This stores the distance between two points for calibration, default value is 100 cm or 1m
        self.measurement = 100
        # This store the points for the center of the gride position
        self.center = [] 
        # This store the points for the puck position
        self.puck = [] 
        # This store the error measurement calculated value from the center to the puck
        self.error_measurement_value = None  
        # This store the difference in x and y coordinates between the center and the puck
        self.diff_x = None
        self.diff_y = None
