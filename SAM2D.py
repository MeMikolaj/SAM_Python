import numpy as np
import math

class SAM2D(object):
    
    def __init__(self):
        pass



class Robot(object):

    def __init__(self) -> None:
        self.time = 10 # how many seconds will it run, how many steps

        # Robot's Pose in W coordinates: x, y, theta
        self.measured_pose = np.zeros((self.time, 3, 1)) # GPS
        self.predicted_pose = np.zeros((self.time, 3, 1)) # Predicted after 1s of control input
        self.estimated_pose = np.zeros((self.time, 3, 1)) # The one that we think it is at
        self.sigma_x = 1 # GPS error 1m
        self.sigma_y = 1

        # Robot's Velocity
        self.velocity = np.zeros((self.time, 2, 1)) # Velocity of Wheel Left and Right in m/s
        self.L = 0.2 # Distance between wheels 0.2 m
        self.sigma_wheel = 0.3 # errorr of the velocity 0.3 m/s each wheel

        # Landmarks ground-truth positions
        landmarks_data = [
                    {"index": 1, "coordinates": [-1, 1]},
                    {"index": 2, "coordinates": [1, 2]},
                    {"index": 3, "coordinates": [3, -1]},
                    {"index": 4, "coordinates": [4, 3]},
                    {"index": 5, "coordinates": [5, 7]},
                    {"index": 6, "coordinates": [6, -4]},
                    {"index": 7, "coordinates": [7, 0]},
                    {"index": 8, "coordinates": [10, 4]},
                    {"index": 9, "coordinates": [12, -3]},
                    {"index": 10, "coordinates": [14, 1]},
                    {"index": 11, "coordinates": [17, 0]}
                    ]
        self.landmarks = np.array(landmarks_data, dtype=object)

        # Robot's Measurements
        self.sigma_measurement_range_x = 0.4 # Lidar range error, includes beam error
        self.sigma_measurement_range_y = 0.4 # Lidar range error, includes beam error
