from kivy.uix.screenmanager import Screen
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.lang import Builder

from main import Xyrox_loop
from engine import Xyrox

engine = Xyrox()
loop = Xyrox_loop()

class ChatScreen(Screen, RelativeLayout):
    Builder.load_file('layouts/chat_layout/chat.kv')

    def __init__(self, **kwargs):

        super(ChatScreen, self).__init__(**kwargs)
            
    def start(self):

        loop.start()

    def stop(self):

        loop.interrupt()
        loop.stop()
    
    def chats(self):

        return 'Text now'
    
    def apply(self):
        loop.apply()

    def close(self):
        App.get_running_app().stop()