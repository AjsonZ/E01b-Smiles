#!/usr/bin/env python3

import utils, open_color, arcade

utils.check_version((3,7))

SCREEN_WIDTH = 800              #set the width of screen 
SCREEN_HEIGHT = 600             #set the height of screen 
SCREEN_TITLE = "Smiley Face Example"            #set the title

class Faces(arcade.Window):             # create a class named Faces and uses arcade and Window
    """ Our custom Window Class"""

    def __init__(self):                 # initialize the class Faces
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)             #Call the parent class initializer

        # Show the mouse cursor
        self.set_mouse_visible(True)

        self.x = SCREEN_WIDTH / 2               #Divide it by 2
        self.y = SCREEN_HEIGHT / 2              #Divide it by 2

        arcade.set_background_color(open_color.white)               # set the background color

    def on_draw(self):              # define on_draw
        """ Draw the face """
        arcade.start_render()       # start the render process. This must be done before any drawing commands
        face_x,face_y = (self.x,self.y)
        smile_x,smile_y = (face_x + 0,face_y - 10)              #set the position of smile
        eye1_x,eye1_y = (face_x - 30,face_y + 20)               #set the position of eye1
        eye2_x,eye2_y = (face_x + 30,face_y + 20)               #set the position of eye2
        catch1_x,catch1_y = (face_x - 25,face_y + 25)           #set the position of catch1
        catch2_x,catch2_y = (face_x + 35,face_y + 25)           #set the position of catch2

        arcade.draw_circle_filled(face_x, face_y, 100, open_color.yellow_3)             #fill the circle with yellow
        arcade.draw_circle_outline(face_x, face_y, 100, open_color.black,4)             #draw the outline of circle with black
        arcade.draw_ellipse_filled(eye1_x,eye1_y,15,25,open_color.black)                #fill the eye1 with black 
        arcade.draw_ellipse_filled(eye2_x,eye2_y,15,25,open_color.black)                #fill the eye2 with black
        arcade.draw_circle_filled(catch1_x,catch1_y,3,open_color.gray_2)                #fill the catch1 with grey
        arcade.draw_circle_filled(catch2_x,catch2_y,3,open_color.gray_2)                #fill the catch2 with grey
        arcade.draw_arc_outline(smile_x,smile_y,60,50,open_color.black,190,350,4)       #draw the smile arc with black


    def on_mouse_motion(self, x, y, dx, dy):                #define on_mouse_motion
        """ Handle Mouse Motion """
        self.x = x
        self.y = y



window = Faces()            #imply and show the window
arcade.run()                #start the program