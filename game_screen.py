from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from player import Player
from utilities import Utils
from kivy.clock import Clock
from ball import Ball
from level_controller import Level_Controller

class GameScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)


        Utils.set_background(self, 'data/home_background.png')
        

        self.ball = Ball(game_screen=self)
        self.add_widget(self.ball)

        self.player = Player(game_screen=self, ball=self.ball)
        self.add_widget(self.player)

        self.level_controller = Level_Controller(self, self.ball)
        self.add_widget(self.level_controller)
        # Game update
        Clock.schedule_interval(self.game_update, 1.0/60.0)
        

        
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        print('Unbound')
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'a':   
            
            self.player.move_left()
        elif keycode[1] == 'd':
            self.player.move_right()
        return True

    def game_update(self, *args):
        self.player.check_constaints()
        
        self.ball.move()
        self.ball.check_constraints()
        self.player.bounce_ball()
        