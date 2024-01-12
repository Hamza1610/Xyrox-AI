from kivy.uix.screenmanager import Screen
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.stacklayout import StackLayout
from kivy.core.window import Window
from kivy.app import App
from kivy.lang import Builder
import sqlite3

from main import Xyrox_loop
from engine import Xyrox
from db_wrapper import DB

engine = Xyrox()
loop = Xyrox_loop()
wrapper = DB('chat_history')

class ChatScreen(Screen, RelativeLayout):
    Builder.load_file('layouts/chat_layout/chat.kv')

    def __init__(self, **kwargs):

        super(ChatScreen, self).__init__(**kwargs)

        wrapper.creat_table('Chats')

            
    def start(self):

        loop.start()

    def stop(self):

        loop.interrupt()
        loop.stop()

    def show_children(self):

        self.chats()

    def chats(self):

        last_ten_chats = wrapper.get_table_last_ten(table_name='Chats')
        try:
            print(last_ten_chats)
            for msg in last_ten_chats:
                new_text_input = TextInput(
                    text= str(msg),
                    height = 350,
                    multiline=False,
                    background_color=(1, .5, .9, .4),
                    foreground_color=(1, 1, 1, 1),
                    border=(2, 2, 2, 2)
                )
                self.ids.chat_box.add_widget(new_text_input)
        except:
            new_text_input = TextInput(
                    text= 'Error loading message',
                    multiline=False,
                    background_color=(1, .5, .9, .4),
                    foreground_color=(1, 1, 1, 1),
                    border=(2, 2, 2, 2)
                )
            self.ids.chat_box.add_widget(new_text_input)

    def apply(self):
        loop.apply()

    def close(self):
        App.get_running_app().stop()