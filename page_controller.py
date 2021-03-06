from kivy.uix.screenmanager import ScreenManager
from game_screen import GameScreen

class PageController(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.initialize_game_screen()
    
    def initialize_game_screen(self):
        self.game_screen = GameScreen()
        self.switch_to(self.game_screen)