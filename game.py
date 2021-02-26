import kivy
from kivy.app import App
from kivy.uix.label import Label
kivy.require('2.0.0')


class FirstApp(App):
    def build(self):
        alabel = Label(text='Hello World')
        alabel.font_size = 40
        return alabel