from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, Rectangle

class ChatApp(App):
    def build(self):
        self.chat_layout = BoxLayout(orientation='vertical', spacing=10)
        self.set_background_color(self.chat_layout, (0.8, 0.8, 0.8, 1))  # Change background color here
        self.scroll_view = ScrollView(size_hint=(1, None), height=400,
                                      bar_width=10, scroll_type=['bars'],
                                      bar_margin=10, bar_color=(0, 0.7, 0.3, 1))
        self.chat_box = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None)

        # Add some initial messages
        self.add_message("User", "Hello, how are you?")
        self.add_message("Xyrox", "I'm doing well, thank you!")

        self.scroll_view.add_widget(self.chat_box)
        self.chat_layout.add_widget(self.scroll_view)

        self.input_box = TextInput(size_hint=(1, None), height=40)
        send_button = Button(text='Send', size_hint=(1, None), height=40)
        send_button.bind(on_press=self.send_message)

        self.chat_layout.add_widget(self.input_box)
        self.chat_layout.add_widget(send_button)

        return self.chat_layout

    def set_background_color(self, widget, color):
        with widget.canvas.before:
            Color(*color)
            Rectangle(pos=widget.pos, size=widget.size)

    def send_message(self, instance):
        user_message = self.input_box.text
        self.add_message("User", user_message)
        # Perform any processing or response generation here
        self.add_message("Xyrox", "I received: " + user_message)
        self.input_box.text = ""

    def add_message(self, username, message):
        message_label = Label(text=f"[b]{username}:[/b] {message}", markup=True)
        self.chat_box.add_widget(message_label)
        self.scroll_view.scroll_y = 0  # Scroll to the bottom after adding a message

if __name__ == '__main__':
    ChatApp().run()
