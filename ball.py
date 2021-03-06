from kivy.core import window
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color, Ellipse
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
import random

from kivy.vector import Vector



class Ball(Widget):

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def __init__(self, game_screen:Widget, **kwargs):
        super().__init__(**kwargs)

        self.size_hint = (.05, .05)
        self.game_screen = game_screen



        self.speed = 2
        

        Clock.schedule_once(self.assign_pos, 1) 

        with self.canvas:
            self.ellipse = Ellipse(pos=self.pos, size=self.size)
            Color(.234, .456, .678, .8)
            self.bind(pos=self.update_rect, size=self.update_rect) 

        self.serve_ball()

    # update function which makes the canvas adjustable. 
    def update_rect(self, *args): 
        self.ellipse.pos = self.pos 
        self.ellipse.size = self.size 

    def assign_pos(self, *args):
        self.pos = (Window.size[0]/2, Window.size[1]/2)
        

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

    def serve_ball(self):
        self.center = self.game_screen.center
        self.velocity = Vector(self.speed, 0).rotate(random.randint(75, 105))

    def check_constraints(self):
        
            # bounce off top and bottom
            if (self.y < 0) or (self.top > self.game_screen.height):
                self.velocity_y *= -1

            # bounce off left and right
            if (self.x < 0) or (self.right > self.game_screen.width):
                self.velocity_x *= -1