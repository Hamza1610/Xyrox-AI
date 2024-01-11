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

engine = Xyrox()
loop = Xyrox_loop()

class ChatScreen(Screen, RelativeLayout):
    Builder.load_file('layouts/chat_layout/chat.kv')

    def __init__(self, **kwargs):

        super(ChatScreen, self).__init__(**kwargs)

        # database
        self.conn = sqlite3.connect('chat_history.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Chats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                User TEXT,
                Text TEXT
            )
        ''')

        self.conn.commit()
            
    def start(self):

        loop.start()
        chat = loop.get_instant_chat()
        if chat.keys() == 'Me':
            self.cursor.execute('INSERT INTO Chats (Users, Text) VALUES (?, ?)', ('Me', chat.values()))
        elif chat.keys() == 'Xyrox':

            self.cursor.execute('INSERT INTO Chats (Users, Text) VALUES (?, ?)', ('Xyrox', chat.values()))
        else:
            self.cursor.execute('INSERT INTO Chats (Users, Text) VALUES (?, ?)', ('Unknown', chat.values()))
    def stop(self):

        loop.interrupt()
        loop.stop()

    def show_children(self):
        self.chats()
    
    def chats(self):
        chats_from_db = self.cursor.fetchall()
        try:
            
            print(chats_from_db)
            for msg in chats_from_db:
                new_text_input = TextInput(
                    text= msg,
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