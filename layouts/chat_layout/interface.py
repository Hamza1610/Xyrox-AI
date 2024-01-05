from kivy.app import App
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.core.window import Window

class InterfaceLayout(RelativeLayout):

    # Set minimum width and height for the entire window
    Window.minimum_width = 800
    Window.minimum_height = 600
    # Load the .kv file
    Builder.load_file('interface.kv')

    def on_button_press(self):
        print("Button pressed!")


class InterfaceApp(App):
    def build(self):
        return InterfaceLayout()

if __name__ == '__main__':
    InterfaceApp().run()
