from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from brick import Brick
from kivy.uix.screenmanager import Screen

class Level_Controller(GridLayout):
    def __init__(self, game_screen:Screen, ball:Widget, **kwargs):
        super().__init__(**kwargs)
        #instantiate ball
        self.ball = ball

        # Instantiate number of boxes per level
        self.number_of_boxes_counter = 5

        # set orientation of box and spacing
        self.spacing = 5
        self.cols = self.number_of_boxes_counter

        # Instantiate game screen
        self.game_screen = game_screen

        # Instantiate level
        self.level = 1

        # Spacing between children in widget
        self.spacing = 10

        # Sizing the widget
        self.size_hint = (1, .3)

        # Placing the widget at top of screen
        self.pos_hint = {'x':0, 'y': .7}
        
        
        
        self.generate_boxes()
        
        

    def generate_boxes(self):
        for i in range(self.number_of_boxes_counter):
            for i in range(self.number_of_boxes_counter):
                box = Brick(self.ball, self)
                self.add_widget(box)
           
            


