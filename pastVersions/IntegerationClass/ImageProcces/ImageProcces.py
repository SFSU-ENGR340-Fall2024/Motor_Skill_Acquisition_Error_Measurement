
from tkinter import simpledialog, messagebox
import tkinter as tk
import numpy as np


class ImageProcess:
    def __init__(self):
        pass

    # Given two points, calculate the pixel distance between them
    # Input: x1, y1, x2, y2 {two points}
    # Output: distance {float} - the pixel distance between the two

    def pixeldistance(self, x1, y1, x2, y2):
        return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    # Given a real-world distance and a pixel distance, calculate the scaling factor
    # Input: real_world_distance, pixel_distance {floats}
    # Output: scaling factor {float}

    def scalingfactor(self, real_world_distance, pixel_distance):
        return real_world_distance / pixel_distance
    
    # Given a scaling factor and a pixel distance, calculate the real-world life error measurement
    # Input: x1, y1, x2, y2, scaling_factor {floats}
    # Output: error {float} - the real-world error measurement between the two points
    def errorcalculation(self, x1, y1, x2, y2, scaling_factor):
        return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) * scaling_factor
    
    # Calculate the real life x and y values that produce error measurement between two points
    # Input: x1, y1, x2, y2, scaling_factor {floats}, center_of_grid 
    # Output: x, y {floats} - the real-life x and y values that produce the error measurement
    def errorcalculationxy(self, x1, y1, x2, y2, scaling_factor):
        return (x2 - x1) * scaling_factor, (y2 - y1) * scaling_factor
    

   

    



    
