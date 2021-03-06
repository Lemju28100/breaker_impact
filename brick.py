from os import fspath
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.vector import Vector
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock



class Brick(Widget):
    def __init__(self, ball:Widget, father:GridLayout, **kwargs):
        super().__init__(**kwargs)
        self.father = father
        self.ball = ball


        self.height = self.father.height/5
        self.width = self.father.width/5

        self.is_removed = False

        # Set player color canvas
        with self.canvas:
            self.color = Color(.234, .456, .678, .8)
            self.rect = Rectangle(pos = self.center, 
                                  size =(self.width / 2., 
                                        self.height / 2.))

            
            self.bind(pos=self.update_rect, size=self.update_rect) 

        self.collision_counter = Clock.schedule_interval(self.collision_enter, 1.0/60.0)

    # update function which makes the canvas adjustable. 
    def update_rect(self, *args): 
        self.rect.pos = self.pos 
        self.rect.size = self.size 

    def assign_pos(self, *args):
        self.pos = (self.game_screen.center_x - self.width/2, self.game_screen.height/15)

    def collision_enter(self, *args):

        if self.collide_widget(self.ball):
            vx, vy = self.ball.velocity
            speedup = 1.01
            offset = (self.ball.center_y - self.center_y)/ (self.height/2)
            
            bounced = Vector(vx, -1 * vy)
            vel = bounced * speedup
            self.ball.velocity = vel.x, vel.y
            Clock.unschedule(self.collision_counter)

            self.canvas.clear()
            self.is_removed = True
            # self = BoxLayout(orientation='horizontal')


            # self.father.parent_boxes[self.parent_id].remove_widget(self)
        