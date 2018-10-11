##
# Copyright 2018, Ammar Ali Khan
# Licensed under MIT.
# Since: v1.0.0
##

import time
import cv2
import numpy as np
from src.common.package.config import application
from src.opencv.package.config import application as _application
from src.common.package.http import server as _server
from src.common.package.http.handler import Handler
from src.common.package.camera.capture import Capture as _capture
from src.common.package.frame.action import Action as _frame
from src.common.package.frame.draw import Draw as _draw
from src.opencv.package.opencv.opencv import OpenCV

# Constant
_opencv = OpenCV()


##
# StreamHandler class - inherit Handler
# This class provide handler for HTTP streaming
# Note: this class should override Handler.stream
##
class StreamHandler(Handler):

    ##
    # Override method Handler.stream()
    ##
    def stream(self):
        Handler.stream(self)
        print('[INFO] Overriding stream method...')

        # Initialise capture
        capture = _capture(src=application.CAPTURING_DEVICE,
                           use_pi_camera=application.USE_PI_CAMERA,
                           resolution=application.RESOLUTION,
                           frame_rate=application.FRAME_RATE)

        if application.USE_PI_CAMERA:
            print('[INFO] Warming up pi camera...')
        else:
            print('[INFO] Warming up camera...')

        time.sleep(2.0)

        print('[INFO] Start capturing...')

        while True:
            # Read a frame from capture
            frame = capture.read()

            # Down size frame to 50% (to increase performance on Raspberry Pi)
            # frame = _frame.scale(frame=frame, scale=0.5)

            # Convert frame to gray (to increase performance on Raspberry Pi)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Get frame dimensions
            (height, width) = frame.shape[:2]

            # OpenCV detection
            detections = _opencv.dnn_face_detector(frame=frame,
                                                   scale_factor=1.0,
                                                   size=(300, 300),
                                                   mean=(104.0, 177.0, 123.0))

            # Up size frame to 50% (how the frame was before down sizing)
            # frame = _frame.scale(frame=frame, scale=2)

            # If returns any detection
            for i in range(0, detections.shape[2]):
                # Get confidence associated with the detection
                confidence = detections[0, 0, i, 2]

                # Filter weak detection
                if confidence < _application.CONFIDENCE:
                    continue

                # Calculate coordinates
                box = detections[0, 0, i, 3:7] * np.array([width,
                                                           height,
                                                           width,
                                                           height])

                (left, top, right, bottom) = box.astype('int')

                coordinates = {'left': left,
                               'top': top,
                               'right': right,
                               'bottom': bottom}

                text = "{:.2f}%".format(confidence * 100)

                frame = _draw.rectangle(frame=frame,
                                        coordinates=coordinates,
                                        text=text)

            # Write date time on the frame
            frame = _draw.text(frame=frame,
                               coordinates={'left': application.WIDTH - 150, 'top': application.HEIGHT - 20},
                               text=time.strftime('%d/%m/%Y %H:%M:%S', time.localtime()),
                               font_color=(0, 0, 255))

            # Convert frame into buffer for streaming
            retval, buffer = cv2.imencode('.jpg', frame)

            # Write buffer to HTML Handler
            self.wfile.write(b'--FRAME\r\n')
            self.send_header('Content-Type', 'image/jpeg')
            self.send_header('Content-Length', len(buffer))
            self.end_headers()
            self.wfile.write(buffer)
            self.wfile.write(b'\r\n')


##
# Method main()
##
def main():
    try:
        address = ('', application.HTTP_PORT)
        server = _server.Server(address, StreamHandler)
        print('[INFO] HTTP server started successfully at %s' % str(server.server_address))
        print('[INFO] Waiting for client to connect to port %s' % str(application.HTTP_PORT))
        server.serve_forever()
    except Exception as e:
        server.socket.close()
        print('[INFO] HTTP server closed successfully.')
        print('[ERROR] Exception: %s' % str(e))


if __name__ == '__main__':
    main()
