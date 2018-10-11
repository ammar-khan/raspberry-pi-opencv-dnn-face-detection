##
# Copyright 2018, Ammar Ali Khan
# Licensed under MIT.
# Since: v1.0.0
##

from imutils.video import VideoStream
from src.common.package.config import default
from src.common.package.config import application


##
# Capture class
# This class will capture single frame from camera.
# It supports USB web camera and Pi camera both
# If using Pi Camera then set USE_PI_CAMERA to True in config.application.py
##
class Capture:

    def __init__(self,
                 src=application.CAPTURING_DEVICE,
                 use_pi_camera=False,
                 resolution=default.RESOLUTION,
                 frame_rate=default.FRAME_RATE):

        self.capture = VideoStream(src=src,
                                   usePiCamera=use_pi_camera,
                                   resolution=resolution,
                                   framerate=frame_rate).start()

    def read(self):
        return self.capture.read()
