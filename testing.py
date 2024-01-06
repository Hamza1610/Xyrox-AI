from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.properties import StringProperty

class WelcomeScreen(RelativeLayout):
    label_text = StringProperty("Welcome back!")  # Initial value

    def __init__(self, **kwargs):
        super(WelcomeScreen, self).__init__(**kwargs)

        # Set up the layout
        box_layout = BoxLayout(
            orientation='vertical',
            width=500,
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )

        # Add label and button to the layout
        label = Label(text=self.label_text, font_size='60sp')
        button = Button(text='Get started with Xyrox', size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5})
        button.bind(on_press=self.on_press_start)

        # Bind the label's text property to the label_text variable
        label.bind(text=self.update_label_text)

        # Add widgets to the layout
        box_layout.add_widget(label)
        box_layout.add_widget(button)

        # Add the layout to the relative layout
        self.add_widget(box_layout)

    def on_press_start(self, instance):
        # Update the label_text variable when the button is pressed
        self.label_text = "New Text!"

    def update_label_text(self, instance, value):
        # Callback function to update the label's text
        instance.text = value

class WelcomeApp(App):
    def build(self):
        return WelcomeScreen()

if __name__ == '__main__':
    WelcomeApp().run()
