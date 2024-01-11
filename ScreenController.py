from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.core.window import Window
from layouts.welcome_layout.welcome import WelcomeScreen
from layouts.chat_layout.chat import ChatScreen


class ScreenController(App):

    def build(self):

         # Set minimum width and height for the entire window
        Window.minimum_width = 800
        Window.minimum_height = 600
        # Create the ScreenManager
        screen_manager = ScreenManager()

        # Create instances of the screens
        welcome_screen = WelcomeScreen(name='welcome')
        chat_screen = ChatScreen(name='chat')

        # Add the screens to the ScreenManager
        screen_manager.add_widget(welcome_screen)
        screen_manager.add_widget(chat_screen)

        return screen_manager


if __name__ == '__main__':
    ScreenController().run()