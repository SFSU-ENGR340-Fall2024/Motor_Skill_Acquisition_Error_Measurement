import cv2
class DataClass:
    def __init__(self, image, width=1500, height=700):
    # This store the image
        self.image = cv2.imread(image)
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
        self.real_dist = None

        # Distance between calibration points
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

    # Return the image
    def get_image(self):
        return self.image
    # Return the resized image
    def get_resized_image(self):
        return self.imageresized
    # Return the original image
    def get_original_image(self):
        return self.original_image
    # Return the calibration points
    def get_points(self):
        return self.points
    # Return the scaling factor
    def get_scaling_factor(self):
        return self.scaling_factor
    # Return the measurement
    def get_measurement(self):
        return self.measurement
    # Return the center points
    def get_center(self):
        return self.center
    # Return the puck points
    def get_puck(self):
        return self.puck
    # Real life Measure
    def get_real_dist(self):
        return self.real_dist
    # Return the error measurement value
    def get_error_measurement_value(self):
        return self.error_measurement_value
    # Return the difference in x coordinates
    def get_diff_x(self):
        return self.diff_x
    # Return the difference in y coordinates
    def get_diff_y(self):
        return self.diff_y
    # Set the image
    def set_image(self, image):
        self.image = image
    # Set the resized image
    def set_resized_image(self, image):
        self.imageresized = image
    # Set the original image
    def set_original_image(self, image):
        self.original_image = image
    # Set real-world distance
    def set_real_dist(self, dist):
        self.real_dist = dist
    # append the calibration points
    def append_points(self, point):
        self.points.append(point)
    # Set the calibration points
    def set_points(self, points):
        self.points = points
    # Set the scaling factor
    def set_scaling_factor(self, scaling_factor):
        self.scaling_factor = scaling_factor
    # Set the measurement
    def set_measurement(self, measurement):
        self.measurement = measurement
    # Set the center points
    def set_center(self, center):
        self.center = center
    # Set the puck points
    def set_puck(self, puck):
        self.puck = puck
    # Set the error measurement value
    def set_error_measurement_value(self, error_measurement_value):
        self.error_measurement_value = error_measurement_value
    # Set the difference in x coordinates
    def set_diff_x(self, diff_x):
        self.diff_x = diff_x
    # Set the difference in y coordinates
    def set_diff_y(self, diff_y):
        self.diff_y = diff_y

