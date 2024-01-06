from kivy.uix.screenmanager import Screen
from kivy.uix.relativelayout import RelativeLayout
from kivy.lang import Builder


class ChatScreen(Screen, RelativeLayout):
    Builder.load_file('layouts/chat_layout/chat.kv')

    def __init__(self, **kwargs):
        super(ChatScreen, self).__init__(**kwargs)

    def on_button_press(self):
        self.manager.current = 'welcome'
        print("Button pressed!")
