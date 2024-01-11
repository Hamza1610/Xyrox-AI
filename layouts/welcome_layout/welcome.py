from kivy.uix.screenmanager import Screen
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

from engine import Xyrox


engine = Xyrox()

class WelcomeScreen(Screen, RelativeLayout):
    Builder.load_file('layouts/welcome_layout/welcome.kv')

    def __init__(self, **kwargs):
        super(WelcomeScreen, self).__init__(**kwargs)

    def on_press_start(self):
        self.manager.current = 'chat'
        # engine.welcome_speech()
        print("Button pressed!")