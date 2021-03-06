import random
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color
from kivy.vector import Vector
from kivy.clock import Clock

class Player(Widget):
    def __init__(self, ball:Widget, game_screen:Screen) -> None:
        super().__init__()

        # Set player size
        self.size_hint_x = .2
        self.size_hint_y = .05
        self.ball = ball
        self.speedup = 1.01



        # SEt player color
        self.color = 0
    
        # Set player velocity
        self.velocity = (20, 0)

        # Initialize game screen
        self.game_screen = game_screen

        # Set player initial position
       
        Clock.schedule_once(self.assign_pos, 2) 

        # Set player color canvas
        with self.canvas:
            Color(.234, .456, .678, .8)
            self.rect = Rectangle(pos = self.center, 
                                  size =(self.width / 2., 
                                        self.height / 2.))

            
            self.bind(pos=self.update_rect, size=self.update_rect) 

    # update function which makes the canvas adjustable. 
    def update_rect(self, *args): 
        self.rect.pos = self.pos 
        self.rect.size = self.size 

    def assign_pos(self, *args):
        self.pos = (self.game_screen.center_x - self.width/2, self.game_screen.height/15)

    # Function to move right
    def move_right(self):
        
        self.pos = tuple(sum(i) for i in zip(self.pos, self.velocity))

    # Function to move left
    def move_left(self):
        
        self.pos = tuple(map(lambda i, j: i - j, self.pos, self.velocity))

    # Function to check borders so player does not go off-screen
    def check_constaints(self, *args):
        
        if (self.x + self.width) > self.game_screen.width:
            self.x = self.game_screen.width - self.width
            


        elif (self.x) < 0:
            self.x = 0

    def bounce_ball(self):
        if self.collide_widget(self.ball):
            vx, vy = self.ball.velocity

            
            offset = (self.ball.center_y - self.center_y)/ (self.height/2)

            if tuple(self.ball.pos) >= (self.x - self.ball.center_x, self.y+self.height) and tuple(self.ball.pos) < (self.x + self.width/4, self.y+self.height):
                print('Hit left', self.ball.velocity)

                bounced = Vector(-1 * vx if vx > 0 else vx, -1 * vy if vy < 0 else vy)

            elif tuple(self.ball.pos) >= (self.x + self.width/4, self.y+self.height) and tuple(self.ball.pos) < (self.x + self.width * 3/4, self.y+self.height):
                print('Hit Middle', self.ball.velocity)
                bounced = Vector(vx, -1 * vy)

            elif tuple(self.ball.pos) >= (self.x + self.width * 3/4, self.y+self.height) and tuple(self.ball.pos) <= (self.x + self.width + self.ball.center_x, self.y+self.height):
                print('Hit right', self.ball.velocity)
                bounced = Vector(-1 * vx if vx < 0 else vx, -1 * vy if vy < 0 else vy)

            else:
                bounced = Vector(vx, -1 * vy)


            vel = bounced * self.speedup
            self.ball.velocity = vel.x, vel.y
            self.speedup+= 0.001
            print(self.speedup)
            

    
    