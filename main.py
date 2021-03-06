from kivy.app import App
from page_controller import PageController
from kivy.config import Config

page_controller = PageController()


class BreakerImpactApp(App):

    def build(self):
        Config.set('graphics', 'width', '600')
        Config.set('graphics', 'height', '600')
        Config.write()
        return page_controller

if __name__ == "__main__":
    BreakerImpactApp().run()





