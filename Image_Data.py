#This is the main class that holds the data for the images
#Each Image is associated with all of the data that is generated using it

#Attributes:
#   image:              The file location of the actual image
#   puck:               A tuple telling us the x, y coordinates of the puck
#   goal:               A tuple telling us the x, y location of the goal
#   error:              A number telling us the distance between the puck and goal
#   result_image:       The location of the results image
#   calibration:        A nubmer telling us the size of each pixel
#   results_folder:     The location of the results folder
#   
#Functions:
#   create_results_image(self)      Create an image identical to the original image
#                                   then add overlay based on the data.
#   
#   get_image(self)                         Return the image
#   get_puck(self)                          Return the puck location
#   get_goal(self)                          Return the goal location
#   get_error(self)                         Return the error
#   get_calibration(self)                   Return the calibration data
#   get_result_image(self)                  Return the results image
#
#   set_puck(self, puck)                    Set puck location
#   set_goal(self, goal)                    Set goal location
#   set_error(self, error)                  Set error
#   set_calibration(self, calibration)      Set calibration data
#   set_results_folder(self, folder)        Set the location of the results folder

import cv2

class Image_Data:
    def __init__(self, image):
        self.image = image
        self.puck = -1
        self.goal = -1
        self.error = -1
        self.calibration = -1
        self.results_image = -1
        self.results_folder = -1

    def create_results_image(self):
        #copy the original image
        results_image = self.image

        #draw a green line between the goal and puck
        cv2.line(results_image, self.puck, self.goal, (0, 255, 0), 3)

        #draw a red circle around the goal and puck
        cv2.circle(results_image, self.goal, 5, (255, 0, 0), 3)
        cv2.circle(results_image, self.puck, 5, (255, 0, 0), 3)

        #return the results image
        return results_image
    
    def get_image(self):
        return self.image
    
    def get_puck(self):
        return self.puck
    
    def get_goal(self):
        return self.goal
    
    def get_error(self):
        return self.error
    
    def get_calibration(self):
        return self.calibration
    
    def get_results_image(self):
        return self.results_image
    
    def get_results_folder(self):
        return self.results_folder
    
    def set_puck(self, puck):
        self.puck = puck
    
    def set_goal(self, goal):
        self.goal = goal

    def set_error(self, error):
        self.error = error

    def set_calibration(self, calibration):
        self.calibration = calibration

    def set_results_folder(self, folder):
        self.results_folder = folder