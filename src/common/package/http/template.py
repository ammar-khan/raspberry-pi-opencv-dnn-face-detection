##
# Copyright 2018, Ammar Ali Khan
# Licensed under MIT.
# Since: v1.0.0
##

from pathlib import Path
from src.common.package.config import application


##
# Template class
# This class provides utility methods for template
##
class Template(object):

    def __init__(self):
        return self

    ##
    # Static method load()
    # Method to load template
    #
    # @param file_name - template file name with extension
    #
    # @return template contents
    ##
    @staticmethod
    def load(file_name):
        template = Path(application.HTML_TEMPLATE_PATH + file_name)

        with open(str(template), 'r') as _file:
            html_template = _file.read().replace('\n', '')
            _file.close()

        return html_template
