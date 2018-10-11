##
# Copyright 2018, Ammar Ali Khan
# Licensed under MIT.
# Since: v1.0.0
##

import numpy as np
import cv2


##
# Action class
##
class Action:

    def __init__(self):
        return self

    ##
    # Static method scale()
    # Method to scale image using aspect ratio
    #
    # @param frame - image frame
    # @param scale - aspect ratio
    #
    # @return frame
    ##
    @staticmethod
    def scale(frame, scale):
        return cv2.resize(frame, (0, 0), fx=scale, fy=scale)

    ##
    # Static method image_to_array()
    # Method to convert image into numpy array (frame)
    #
    # @param image - image
    #
    # @return frame
    ##
    @staticmethod
    def image_to_array(image):
        return np.array(image)