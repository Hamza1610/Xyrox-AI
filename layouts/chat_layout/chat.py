from kivy.uix.screenmanager import Screen
from kivy.uix.relativelayout import RelativeLayout
from kivy.lang import Builder

from main import Xyrox_loop

loop = Xyrox_loop()

class ChatScreen(Screen, RelativeLayout):
    Builder.load_file('layouts/chat_layout/chat.kv')

    def __init__(self, **kwargs):
        super(ChatScreen, self).__init__(**kwargs)

    def on_start_ai(self):
        loop.run()
        print("Xrox loop started!")
