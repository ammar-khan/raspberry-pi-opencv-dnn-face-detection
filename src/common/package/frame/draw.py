##
# Copyright 2018, Ammar Ali Khan
# Licensed under MIT.
# Since: v1.0.0
##

from PIL import Image, ImageDraw, ImageFont
from src.common.package.frame.action import Action
from src.common.package.config import default

# Constant
FONT = ImageFont.truetype(default.FONT_NAME, default.FONT_SIZE)


##
# Draw class
##
class Draw:

    def __init__(self):
        return self

    ##
    # Static method text()
    # Method to write text on frame
    #
    # @param frame - image frame
    # @param coordinates - left and top coordinates
    # @param text - text to write
    # @param font_color - font colour
    # @param font - font
    #
    # @return frame
    ##
    @staticmethod
    def text(frame,
             coordinates,
             text,
             font_color=default.FONT_COLOR,
             font=FONT):

        # Convert frame into image and make it ready to draw
        image = Image.fromarray(frame)
        draw = ImageDraw.Draw(image)

        # Draw
        draw.text((coordinates['left'], coordinates['top']),
                  text,
                  font=font,
                  fill=font_color)

        # Clear
        del draw

        # Convert image to numpy array (frame) and return
        return Action.image_to_array(image)

    ##
    # Static method rectangle()
    # Method to write text on frame
    #
    # @param frame - image frame
    # @param coordinates - left, top, right, bottom coordinates
    # @param text - text to write
    # @param solid - boolean value to make solid box (default False)
    # box_color - box colour
    # @param font_color - font colour
    # @param font - font
    #
    # @return frame
    ##
    @staticmethod
    def rectangle(frame,
                  coordinates,
                  text='',
                  solid=False,
                  box_color=default.BACKGROUND_COLOR,
                  font_color=default.FONT_COLOR,
                  font=FONT):

        # Convert frame into image and make it ready to draw
        image = Image.fromarray(frame)
        draw = ImageDraw.Draw(image)

        if solid:
            # Draw solid
            draw.rectangle(((coordinates['left'], coordinates['top']),
                            (coordinates['right'], coordinates['bottom'])),
                           fill=box_color,
                           outline=box_color)
        else:
            # Draw hollow
            draw.rectangle(((coordinates['left'], coordinates['top']),
                            (coordinates['right'], coordinates['bottom'])),
                           outline=box_color)

        if text:
            text_width, text_height = draw.textsize(text)
            text_x = ((coordinates['left'] + coordinates['right']) - text_width / 2) / 2 - 12
            text_y = coordinates['bottom'] - text_height - 5

            # Draw solid box
            draw.rectangle(((coordinates['left'], coordinates['bottom'] - text_height - 10),
                            (coordinates['right'], coordinates['bottom'])),
                           fill=box_color,
                           outline=box_color)

            # Draw center aligned text
            draw.text((text_x, text_y),
                      text,
                      font=font,
                      fill=font_color)

        # Clear
        del draw

        # Convert image to numpy array (frame) and return
        return Action.image_to_array(image)

    ##
    # Static method circle()
    # Method to draw circle on frame
    #
    # @param frame - image frame
    # @param coordinates - left and top coordinates
    # @param radius - radius
    # @param color - background color
    #
    # @return frame
    ##
    @staticmethod
    def circle(frame,
               coordinates,
               radius,
               color=default.BACKGROUND_COLOR):

        # Convert frame into image and make it ready to draw
        image = Image.fromarray(frame)
        draw = ImageDraw.Draw(image)

        # Draw
        draw.ellipse((coordinates['left'] - radius, coordinates['top'] - radius,
                      coordinates['left'] + radius, coordinates['top'] + radius),
                     fill=color)
        # Clear
        del draw

        # Convert image to numpy array (frame) and return
        return Action.image_to_array(image)