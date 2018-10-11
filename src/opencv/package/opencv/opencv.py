##
# Copyright 2018, Ammar Ali Khan
# Licensed under MIT.
# Since: v1.0.0
##

import cv2
from src.opencv.package.config import application


##
# OpenCV class
# This class is a wrapper for Open Source Computer Vision (OpenCV)
#
# @see: https://opencv.org/
##
class OpenCV:

    def __init__(self):
        print('[INFO] OpenCV - Initialising...')

        self._haarcascade_frontalface_default = cv2.CascadeClassifier(
            application.HAARCASCADE_FRONTALFACE_DEFAULT_PATH
        )

        self._net = cv2.dnn.readNetFromCaffe(
            application.PROTOTEXT_PATH,
            application.MODEL_PATH
        )

    ##
    # Method haarcascade_frontalface_default_detector()
    # Method to return OpenCV haarcascade_frontalface_default_detector
    #
    # @param frame - image frame
    # @param scale_factor - reduce image
    # @param min_neighbours - min neighbours for detections
    # @param min_size - min size of object to detect
    #
    # @return Array of detection(s)
    ##
    def haarcascade_frontalface_default_detector(self,
                                                 frame,
                                                 scale_factor=1.1,
                                                 min_neighbours=5,
                                                 min_size=(30, 30)):

        return self._haarcascade_frontalface_default.detectMultiScale(image=frame,
                                                                      scaleFactor=scale_factor,
                                                                      minNeighbors=min_neighbours,
                                                                      minSize=min_size)

    def dnn_face_detector(self,
                          frame,
                          scale_factor=1.0,
                          size=(300, 300),
                          mean=(104.0, 177.0, 123.0),
                          swap_rb=True):

        # Convert frame to a blob
        blob = cv2.dnn.blobFromImage(image=cv2.resize(frame, size),
                                     scalefactor=scale_factor,
                                     size=size,
                                     mean=mean)

        # Pass the blob through the network and obtain the detections and predictions
        self._net.setInput(blob)
        return self._net.forward()

