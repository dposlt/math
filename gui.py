#! /usr/bin/python env

from kivy.app import App
from kivy.uix.label import Label

class Screen(App):
    def build(self):
        return Label(text="DIVMOD")


if __name__ == "__main__":
    Screen().run()