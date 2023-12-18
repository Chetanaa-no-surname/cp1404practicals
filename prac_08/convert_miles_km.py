"""
CP1404/CP5632 Practical
Miles to Kilometres Converter
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

DIFFERENCE = 1
KM_CONSTANT = 1.60934


class DistanceConvertorApp(App):
    """ DistanceConvertorApp is a Kivy App for conversion between miles and km """
    message = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (300, 200)
        self.title = "Distance converter"
        self.root = Builder.load_file("convert_miles_km.kv")
        self.message = ""
        return self.root

    def output_message(self):
        self.message = self.root.ids.output_label.text

    def handle_increase(self):
        if self.root.ids.num_input.text == "":
            self.root.ids.num_input.text = "0"
        self.root.ids.num_input.text = str(int(self.root.ids.num_input.text) + DIFFERENCE)

    def handle_decrease(self):
        if self.root.ids.num_input.text == "":
            self.root.ids.num_input.text = "0"
        self.root.ids.num_input.text = str(int(self.root.ids.num_input.text) - DIFFERENCE)

    def convert(self):
        try:
            self.message = str(float(self.root.ids.num_input.text) * KM_CONSTANT)
        except ValueError:
            self.message = "0.0"


DistanceConvertorApp().run()
