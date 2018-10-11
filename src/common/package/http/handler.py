##
# Copyright 2018, Ammar Ali Khan
# Licensed under MIT.
# Since: v1.0.0
##

from http import server
from src.common.package.http.template import Template

# Constant
HTML_TEMPLATE = Template.load('index.html')


##
# Handler class - inherits server.BaseHTTPRequestHandler
# This class provide handler for HTTP request
##
class Handler(server.BaseHTTPRequestHandler):

    ##
    # Method stream()
    # Method to override
    ##
    def stream(self):
        return self

    ##
    # Method do_GET()
    # Handle HTTP method Get
    ##
    def do_GET(self):
        if self.path == '/':
            self.send_response(301)
            self.send_header('Location', '/index.html')
            self.end_headers()
        elif self.path == '/index.html':
            content = HTML_TEMPLATE.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(content)
        elif self.path == '/stream.mjpg':
            self.send_response(200)
            self.send_header('Age', 0)
            self.send_header('Cache-Control', 'no-cache, private')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
            self.end_headers()
            try:
                self.stream()
            except Exception as e:
                print('[ERROR] Exception %s: %s' % (self.client_address, str(e)))
        else:
            self.send_error(404)
            self.end_headers()
